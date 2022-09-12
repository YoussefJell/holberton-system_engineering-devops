#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
from json import dumps
import requests
from sys import argv

try:
    int(argv[1])
except Exception as e:
    exit(1)

employeeID = int(argv[1])
endpoint = "https://jsonplaceholder.typicode.com"
user = requests.get("{}/users/{}".format(endpoint, employeeID)).json()
todo = requests.get("{}/users/{}/todos".format(endpoint, employeeID)).json()
employeeName = user.get('name')

row = []

for elem in todo:
    dict = {
        "task": elem.get('title'),
        "completed": elem.get('completed'),
        "username": employeeName
    }
    row.append(dict)

employeeDict = {employeeID: row}

with open('{}.json'.format(employeeID), 'w', encoding="utf-8") as file:
    file.write(dumps(employeeDict))
