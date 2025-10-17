resource "aws_key_pair" "this" {
  key_name   = "${var.env_name}-key"
  public_key = file(var.public_key_path)
}

resource "aws_security_group" "nginx_sg" {
  name        = "${var.env_name}-nginx-sg"
  description = "Allow HTTP and SSH"

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.env_name}-sg"
  }
}

resource "aws_instance" "nginx_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = aws_key_pair.this.key_name
  vpc_security_group_ids = [aws_security_group.nginx_sg.id]

  user_data = file("userdata.sh")

  tags = {
    Name = "${var.env_name}-nginx"
  }
}