import boto3
import json 

ec2_client= boto3.client("ec2") #give ec2 access
response = ec2_client.describe_regions()
print(response["Regions"]) #print the list of regions

def get_regions():
    regions = []
    for response in ec2_client.describe_regions()["Regions"]:
        regions.append(response["RegionName"])
    return regions

get_regions()

with open("aws_regions_ec2.json", "w") as file:
    json.dump(get_regions(), file)


response2 = ec2_client.describe_availability_zones()
print(response2["AvailabilityZones"]) #print the list of availability zones

for response in ec2_client.describe_availability_zones()["AvailabilityZones"]:
    print(response["ZoneName"])

response3 = ec2_client.describe_instances() 
# print(response3["Reservations"]) #print the list of reservations

for response in ec2_client.describe_instances()["Reservations"]:
    for tag in response["Instances"][0]["Tags"]:
        print(tag["Key"], tag["Value"]) 