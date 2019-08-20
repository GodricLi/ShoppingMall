# coding:utf-8

import json


def data_a():
    data_account = {
            "id": 'alex',
            "quota": 20000,
            "password": "abc",
            "status": 0}

    with open('alex.json', 'w') as f:
        json.dump(data_account, f)
    data_account1 = {
        "id": 'luffy',
        "quota": 20000,
        "password": "abc",
        "status": 0}

    with open('luffy.json', 'w') as f1:
        json.dump(data_account1, f1)


data_a()
