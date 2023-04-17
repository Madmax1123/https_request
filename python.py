# -*- coding: utf-8 -*-
import urllib.request
import requests
import json

class user:
    email = 'email'
    password = 'password'

user1 = user()
user1.email = 'admin@admin.com'    
user1.password = '12345'
usr = json.dumps(user1.__dict__)    

headers = {
    'Content-Type': 'application/json',
    'X-eBirdApiToken': 'NaN',
}

url = requests.post("http://137.184.45.229:3001/api/v1/auth/login", usr, headers)


print(url.text)