# coding:utf-8


import os
from .db_handler import load_account
from conf import settings


def land(account, password):
    """验证账户是否存在、密码是否正确,账户是否被冻结"""
    account_file = os.path.join(settings.DB_ACCOUNT, 'lock.txt')
    if os.path.isfile(account_file):                # 锁定账户文件存在
        with open('%s\lock.txt' % settings.DB_ACCOUNT, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                data = line.strip('\n')
                if account in data:
                    exit('账户-%s已被冻结' % account)
                else:
                    account_data = load_account(account)   # load_account的返回值，即账户数据
                    if account_data:
                        if password == account_data['password']:
                            return account_data

    else:   # 不存在锁定账户的文件
        account_data = load_account(account)  # load_account的返回值，即账户数据
        if account_data:
            if password == account_data['password']:
                return account_data










