#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import csv
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

with open('{}.csv'.format(employeeID), 'w', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    for elem in todo:
        row = [employeeID, employeeName, elem.get(
            'completed'), elem.get('title')]
        writer.writerow(row)
