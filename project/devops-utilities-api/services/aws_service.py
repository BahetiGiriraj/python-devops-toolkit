import boto3
from datetime import datetime, timezone, timedelta

def get_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()["Buckets"]

    current_date = datetime.now(timezone.utc).astimezone()
    old_buckets = []
    new_buckets = []
    for bucket in response:
        create_date = bucket['CreationDate']
        days_ago_90 = current_date - timedelta(days=90)
        if create_date < days_ago_90:
            old_buckets.append(bucket['Name'])
        else:
            new_buckets.append(bucket['Name'])


    return {
       "total_buckets": len(new_buckets) + len(old_buckets),
       "new_buckets": new_buckets,
       "old_buckets": old_buckets
   }

get_buckets()