#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
from json import dumps
import requests

endpoint = "https://jsonplaceholder.typicode.com"
users = requests.get("{}/users".format(endpoint)).json()
users_count = len(users)
with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
    for i in range(1, users_count):
        employeeName = users[i].get('name')
        todo = requests.get(
            "{}/users/{}/todos".format(endpoint, i)).json()
        row = []

        for elem in todo:
            dict = {
                "username": employeeName,
                "task": elem.get('title'),
                "completed": elem.get('completed')
            }
            row.append(dict)
        employeeDict = {i: row}

        file.write(dumps(employeeDict))
