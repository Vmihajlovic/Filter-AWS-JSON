import json
import requests

#Program to retrieve AWS JSON file and print appropriate IP ranges
url = 'https://ip-ranges.amazonaws.com/ip-ranges.json' # location of the JSON file from AWS
response = requests.get(url) #saves the response
data = response.json() #saves json to python object

masterList = data['prefixes']

regionInput = input("enter your region: ")
#serviceInput = input("enter your service: ")

for i, entry in enumerate(masterList):
    if entry['service'] == 'EC2' and entry['region'] == regionInput:
        print(entry['service'],entry['ip_prefix'],entry['region']);
    




#object = dict (the json file)
#Array = list (Prefixes)
#This list is made up of objects(dicts?) which each have three strings
#keys for the dicts that are in the list are ip_prefix, region and service
