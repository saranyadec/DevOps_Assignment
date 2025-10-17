variable "aws_region" {
  description = "AWS region to deploy"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for the instance"
  type        = string
  # Example for Amazon Linux 2 in ap-south-1
  default     = "ami-0c2af51e265bd5e0e"
}

variable "env_name" {
  description = "Environment name (e.g., dev, prod)"
  type        = string
}

variable "public_key_path" {
  description = "Path to SSH public key file"
  type        = string
}
 