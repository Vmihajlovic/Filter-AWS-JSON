import json
import requests
from tabulate import tabulate

#Program to retrieve AWS JSON file and print appropriate IP ranges
#this will only retrieve EC2 services
url = 'https://ip-ranges.amazonaws.com/ip-ranges.json' # location of the JSON file from AWS
response = requests.get(url) #saves the response
data = response.json() #saves json to python object

masterList = data['prefixes']

regions = [["Asburn", "us-east-1"],["Palo Alto", "us-west-1"],["Portland","us-west-2"],["Singapore","ap-southeast-1"],["Sydney","ap-southeast-2"],["Tokyo","ap-northeast-1"],["Dublin","eu-west-1"],["Sao Paulo","sa-east-1"]]
print("Region List: \n",tabulate(regions))
      
regionInput = input("enter your region: ")
#serviceInput = input("enter your service: ")

#EC2 service is hardcoded below
for i, entry in enumerate(masterList):
    if entry['service'] == 'EC2' and entry['region'] == regionInput:
#        print(entry['service'],entry['ip_prefix'],entry['region']);
        print(entry['ip_prefix']);
    

