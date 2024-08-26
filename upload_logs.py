#!/usr/bin/python3.9
import boto3
import os
import datetime

#S3 Configuration
BUCKET_NAME = 'i-am-log-sucker'  
S3_FOLDER = 'httpd-logs/'
LOG_FILE_PATH = '/var/log/httpd/error_log' 

#S3 client
s3 = boto3.client('s3')

def upload_logs():
    if os.path.exists(LOG_FILE_PATH):
        # Generate a filename for S3 using the datetime module
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        s3_file_name = f"{S3_FOLDER}access_log_{timestamp}.log"
        
        # Upload the file
        s3.upload_file(LOG_FILE_PATH, BUCKET_NAME, s3_file_name)
        print(f"Uploaded {LOG_FILE_PATH} to s3://{BUCKET_NAME}/{s3_file_name}")
    else:
        print(f"Log file {LOG_FILE_PATH} does not exist.")

upload_logs()
