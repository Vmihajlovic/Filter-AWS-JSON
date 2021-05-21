import time
import requests
from tabulate import tabulate

# Program to retrieve AWS JSON file and print appropriate IP ranges
# this will only retrieve EC2 services
# retrieve the file and save it to a python object
url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
response = requests.get(url)
data = response.json()
f = open("IPranges.txt","w+")
# Retrieve the sync token from the json file, which is epoch time
# convert it to a readable date time
epochTime = int(data['syncToken'])
convertedTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))

# Store the data from the 'prefixes' array
addressData = data['prefixes']

# regions from http://docs.aws.amazon.com/general/latest/gr/rande.html
regions = [["Ashburn", "us-east-1"], ["Palo Alto", "us-west-1"],
        ["Columbus", "us-east-2"], ["Montreal", "ca-central-1"],
        ["Stockholm", "eu-north-1"],["Frankfurt", "eu-central-1"],
        ["London","eu-west-2"],["Paris","eu-west-3"],
        ["Hong Kong", "ap-east-1"],["Mumbai","ap-south-1"],
        ["Portland", "us-west-2"], ["Singapore", "ap-southeast-1"],
        ["Sydney", "ap-southeast-2"], ["Tokyo", "ap-northeast-1"],
        ["Dublin", "eu-west-1"], ["Sao Paulo", "sa-east-1"],
        ["Seoul","ap-northeast-2"],]


print("This list was last updated: ", convertedTime)
print("Region List: \n", tabulate(regions))
regionInput = input("enter your region code (i.e. us-east-1): ")

# EC2 service is hardcoded below
for i, entry in enumerate(addressData):
    if entry['service'] == 'EC2' and entry['region'] == regionInput:
        #        print(entry['service'],entry['ip_prefix'],entry['region']);
        print(entry['ip_prefix']),
        f.write(entry['ip_prefix'])
f.close()
      
