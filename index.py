import os
from dotenv import load_dotenv

load_dotenv(".env")


aws_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
host = os.getenv("AWS_HOST")
db_name = os.getenv("AWS_DATABASE")
user_name = os.getenv("AWS_USER")
password = os.getenv("AWS_PASSWORD")


