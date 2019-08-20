# coding:utf-8


from .db_handler import load_account, save_db
from .logger import access_logger, transaction_logger
from conf import settings
from .admin import add_account, set_account, lock_account


def view_account_info(account):
    """查看账户信息"""
    data = load_account(account)     # 加载账户数据
    print('\033[32;1mACCOUNT INFO\033[0m'.center(50, '-'))
    for k, v in data.items():
        if k not in 'password':
            print('%15s:%s' % (k, v))
    print('\033[32;1mEND\033[0m'.center(50, '-'))
    access_logger.info('查看用户-%s信息' % account)


def repay(account):
    """用户还款"""
    data = load_account(account)
    amount = input('请输入还款金额：').strip()
    if amount.isdigit():
        amount = float(amount)
        data['quota'] = data['quota'] + amount
        save_db(data)
        transaction_logger.info('%s账户还款%s' % (account, amount))
        print('\033[32;1m操作成功\033[0m')
    else:
        print('输入错误')


def withdraw(account):
    """账户提现"""
    data = load_account(account)
    amount = input('请输入提现金额:').strip()
    if amount.isdigit():
        amount = float(amount)
        if 0 < amount < data['quota'] * (1-settings.TRANSACTION_INTEREST):
            data['quota'] = data['quota'] - (amount * (1+settings.TRANSACTION_INTEREST))
            save_db(data)
            transaction_logger.info('%s账户取现%s' % (account, amount))
            print('\033[32;1m操作成功\033[0m')
        else:
            print('取现金额不能大于额度%s' % data['quota'])
    else:
        print('输入错误')


def transfer(account):
    """账户间转帐"""
    data = load_account(account)
    amount = input('请输入转帐金额:').strip()
    if amount.isdigit():
        amount = float(amount)
    account_name = input('请输入转入账户:').strip()
    data_transfer = load_account(account_name)
    if data_transfer:
        if 0 < amount <= data['quota']:
            data['quota'] = data['quota'] - amount
            data_transfer['quota'] = data_transfer['quota'] + amount
            save_db(data_transfer)
            save_db(data)
            transaction_logger.info('%s账户转账%s至%s账户' % (account, amount, data_transfer['id']))
            print('\033[32;1m操作成功\033[0m')
    else:
        print('账户输入错误')


def admin_account(*args):
    """管理账户接口"""
    while True:
        admin_inter = [
                        ('添加账户', add_account),
                        ('用户额度', set_account),
                        ('冻结账户', lock_account)
                                                    ]
        print('\033[32;1mADMIN\033[0m'.center(50, '-'))
        for index, i in enumerate(admin_inter):
            print('\033[32;1m%s:%s\033[0m' % (index, i[0]))
        print('\033[32;1mEND\033[0m'.center(50, '-'))
        choice = input('>>:').strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(admin_inter):
                admin_inter[choice][1](*args)
        elif choice == 'exit':
            exit('bye')
        else:
            print('输入错误')
