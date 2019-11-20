import requests
import json
import demjson
import parser
import mysql.connector
from mysql.connector import Error
a = 157247
response = requests.get("https://api.stackexchange.com//2.2/users/"+str(a)+"/comments?order=desc&sort=creation&site=stackoverflow")
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())