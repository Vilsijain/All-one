import os
import boto3
import botocore

s3 = boto3.client('s3')
def download_from_s3(bucket_name,key_name,download_file_name):
    try:
        with open(f'{download_file_name}', 'wb') as data:
            s3.download_fileobj(bucket_name, key_name, data)
        return download_file_name
    except botocore.exceptions.ClientError as error:
        print('Some error occurred ',error.response['Error']['Code'])
    except Exception as e:
        print(f'Some error occurred {e}')

