# from PIL import Image

# image1 = Image.open(r'C:\Users\Simran\Pictures\Saved Pictures\13586.jpg')
# im1 = image1.convert('RGB')
# im1.save(r'C:\Users\Simran\Pictures\Saved Pictures\new_file_name.pdf')

import os
import s3fs
import argparse
import boto3
import s3file


# S3 bucket info
input_archive_folder = "input_archive"
s3 = s3fs.S3FileSystem(anon=False)
s3_client = boto3.client('s3')

    
def lambda_handler(event, context):
    print("Received event: \n" + str(event))
    for record in event['Records']:
        # Assign some variables that make it easier to work with the data in the 
        # event record.
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        key_url = record['s3']['object']['object_url']
        input_file = os.path.join(bucket,key)
        # archive_path = os.path.join(bucket,input_archive_folder,os.path.basename(key))
        archive_path = os.path.join(bucket,input_archive_folder,'file-jpg-to-pdf.pdf')
        
        jpg_data = jpg_read(input_file)
        # zip_data = zip_read(args)
        write_file(jpg_data,archive_path,bucket,key_url)

def jpg_read(args):
    jpg_file = s3.open(args, 'r')
    # jpg_data = jpg_file.read()
    # jpg_file.close()
    return jpg_file

def zip_read(args):
    zip_file = open(args.zipfile, 'rb')
    zip_data = zip_file.read()
    zip_file.close()

def write_file(jpg_data,archive_path,bucket,key_url):
    
    print("archive_path :",key_url)
    # new_file = s3.open(archive_path, 'w')
    # s3_client.put_object(Body=jpg_data, Bucket=bucket, Key=archive_path)
    # s3_client.upload_file(archive_path, key)
    # s3file.write(new_file,jpg_data)
    # s3.rm(new_file)
    
    new_file = open(key_url, 'wb')
    new_file.write(jpg_data)
    # new_file.write(zip_data)
    new_file.close()








