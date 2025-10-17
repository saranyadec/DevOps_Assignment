# provider.tf

terraform {
  required_version = ">= 1.5.0"

  backend "s3" {
    bucket         = "assignment-state-tf-file"   # your S3 bucket
    key            = "terraform.tfstate"          # path to store state file
    region         = "ap-south-1"                # replace with your bucket region
    encrypt        = true                         # encrypt the state file
    dynamodb_table = ""                           # optional: for state locking, add a DynamoDB table
  }
}

provider "aws" {
  region  = "ap-south-1"                          # your desired AWS region
  profile = "default"                             # optional: if using AWS CLI profile
}
