# coding:utf-8


import json
import os
from conf import settings


def load_account(account):
    """根据account找到对应的账户文件，并读取信息"""
    account_file = os.path.join(settings.DB_ACCOUNT, '%s.json' % account)   # 账户文件路径
    if os.path.isfile(account_file):            # 判断文件路径是否存在
        with open(account_file, 'r') as f:
            data = json.load(f)
            return data                          # 读取出来的账户数据
    else:
        return None


def save_db(data):
    """保存账户数据：
    data = {"id": account, "status": "0"...}"""
    account_file = os.path.join(settings.DB_ACCOUNT, '%s.json' % data['id'])
    f = open(account_file, 'w', encoding='utf-8')
    json.dump(data, f)
    f.close()






