import boto3
import json


s3_client = boto3.client("s3") #give s3 access 

response = s3_client.list_buckets() #list all buckets in s3
print(response["Buckets"]) #print the list of buckets

def get_buckets():
    #option 1 
    # buckets = []
    # for response in s3_client.list_buckets()["Buckets"]:
        # buckets.append(response["Name"])

    # option 2 
    for response in s3_client.list_buckets()["Buckets"]:
     return response["Name"]

get_buckets()

with open("aws_buckets_s3.json", "w") as file:
    json.dump(get_buckets(), file)


