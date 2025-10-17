import boto3
import os
import logging
from botocore.exceptions import BotoCoreError, ClientError
import math
from datetime import datetime

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def upload_file_s3(file_path, bucket, key=None):
    s3 = boto3.client('s3')

    if not key:
        key = os.path.basename(file_path)

    file_size = os.path.getsize(file_path)
    logger.info(f"Uploading {file_path} ({file_size / (1024*1024):.2f} MB)")

    try:
        if file_size > 100 * 1024 * 1024:
            multipart_upload(s3, file_path, bucket, key)
        else:
            s3.upload_file(file_path, bucket, key)
        logger.info(f"Upload successful: {key}")
        presigned_url = s3.generate_presigned_url(
            'get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=3600
        )
        return {"status": "success", "key": key, "presigned_url": presigned_url}
    except (BotoCoreError, ClientError) as e:
        logger.error(f"Upload failed: {e}")
        return {"status": "error", "message": str(e)}

def multipart_upload(s3_client, file_path, bucket, key, part_size=10*1024*1024):
    file_size = os.path.getsize(file_path)
    part_count = math.ceil(file_size / part_size)

    mpu = s3_client.create_multipart_upload(Bucket=bucket, Key=key)
    upload_id = mpu['UploadId']
    parts = []

    try:
        with open(file_path, 'rb') as f:
            for i in range(1, part_count + 1):
                data = f.read(part_size)
                part = s3_client.upload_part(
                    Bucket=bucket,
                    Key=key,
                    PartNumber=i,
                    UploadId=upload_id,
                    Body=data
                )
                parts.append({'ETag': part['ETag'], 'PartNumber': i})

        s3_client.complete_multipart_upload(
            Bucket=bucket,
            Key=key,
            UploadId=upload_id,
            MultipartUpload={'Parts': parts}
        )
    except Exception as e:
        logger.error(f"Multipart upload failed: {e}")
        s3_client.abort_multipart_upload(Bucket=bucket, Key=key, UploadId=upload_id)
        raise

# Lambda handler
def lambda_handler(event, context):
    """
    event example:
    {
        "bucket": "assignment-state-tf-file",
        "file_path": "/tmp/myfile.log",
        "key": "upload_multipart/"
    }
    """
    bucket = event['bucket']
    file_path = event['file_path']
    key = event.get('key')

    result = upload_file_s3(file_path, bucket, key)
    return result
