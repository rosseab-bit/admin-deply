# -*- coding: utf-8 -*-
import requests
import json

url = 'http://localhost:5000/api/signup'
username = "admin"
password = "1234"
data = {"username": username, "password": password}
response = requests.post(url, json=data)
token = json.loads(response.content.decode("utf8"))["token"]
print(token)

urlpost='http://192.168.0.161:3000/api/listapp'
data={"token":token}
dataGet=requests.post(urlpost, json=data)
print(dataGet.content.decode("utf8"))
