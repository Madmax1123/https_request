# -*- coding: utf-8 -*-
import requests
from infos import all_info

post_url = "http://137.184.45.229:3001/api/v1/auth/login"

info = (all_info.dbs.data)
headers = (all_info.dbs.headers)

response = requests.post(post_url, json=info, headers=headers)
query = "INSERT INTO emails (email, password, response) VALUES (%s, %s, %s)"

values = (info['email'], info['password'], response.text)


all_info.dbs.cursor.execute(query, values)
all_info.dbs.db.commit()

print(values)