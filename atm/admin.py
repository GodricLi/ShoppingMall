# coding:utf-8


from .db_handler import load_account, save_db
from .logger import access_logger
from conf import settings


def add_account(*args):
    """添加账户"""
    account = input('添加账户名:').strip()
    password = input('设置密码:').strip()
    quota = input('设置额度:').strip()
    account_data = load_account(account)
    if account_data:
        print('账户已存在')
    else:
        if quota.isdigit():
            quota = float(quota)
            data = {"id": account,
                    "quota": quota,
                    "password": password,
                    "status": 0,
                    "car": []}
            save_db(data)
            access_logger.info('添加账户-%s' % account)
            print('\033[32;1m操作成功\033[0m')
        else:
            print('额度输入错误')


def set_account(*args):
    """设置账户额度"""
    account = input('输入账户名：').strip()
    data = load_account(account)
    if data:
        quota = input('设置额度:')
        if quota.isdigit():
            quota = float(quota)
            data['quota'] = quota
            save_db(data)
            access_logger.info('账户-%s的额度设置为：%s' % (account, data['quota']))
            print('\033[32;1m操作成功\033[0m')
    else:
        print('账户不存在')


def lock_account(*args):
    """锁定用户"""
    account = input('输入账户名：')
    data = load_account(account)
    if data:
        with open('%s\lock.txt' % settings.DB_ACCOUNT, 'a') as f:
            f.writelines(data['id']+'\n')
            access_logger.info('冻结账户名-%s' % data['id'])
            print('\033[32;1m操作成功\033[0m')
    else:
        print('账户名不存在')


