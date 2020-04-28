# Python3.7
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        # print(bucket["Name"])
        return {
        "statuscode": 200,
        "body": json.dumps(
            {"message": bucket['Name']}
        )
    }

# ec2client = boto3.client('ec2')

# def lambda_handler(event, context):
#     regionRes = ec2client.describe_regions()
#     return {
#         "statuscode": 200,
#         "body": json.dumps(
#             {"message": regionRes['Regions']}
#         )
#     }

