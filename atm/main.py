# coding:utf-8


from .landing import land
from .logger import access_logger
from atm import transaction
from shopping_mall import shopping


def conroller(account):
    """查看功能"""
    while True:
        menu = [
                ('账户信息', transaction.view_account_info),
                ('还款', transaction.repay),
                ('取现', transaction.withdraw),
                ('转账', transaction.transfer),
                ('管理', transaction.admin_account),
                ('购物商场', shopping.shopping)
                                                            ]
        print('\033[32;1mMENU\033[0m'.center(50, '-'))
        for index, i in enumerate(menu):
            print('\033[32;1m%s:%s\033[0m' % (index, i[0]))
        print('\033[32;1mEND\033[0m'.center(50, '-'))
        choice = input('>>:').strip()
        if not choice:
            continue
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(menu):
                menu[choice][1](account)
        elif choice == 'exit':
            exit('bye')
        else:
            print('输入错误')


def login(func):

    def inner():
        """用户验证"""
        count = 0
        while count < 3:
            account = input('\033[32;1mAccount:\033[0m').strip()
            password = input('\033[32;1mPassword:\033[0m').strip()
            load_data = land(account, password)
            if load_data:
                if password == load_data['password']:
                    func()
                    access_logger.info('user - %s just logged in' % account)
                    conroller(account)
                    return account
                else:
                    print('账户密码错误')
            else:
                print('账户不存在或密码错误')
            count += 1
            if count == 3:
                msg = 'user-%s tried wrong password reach 3 times' % account
                print(msg)
                access_logger.info(msg)
                break
    return inner


@login
def enter():
    """入口程序"""
    print('\033[32;1mWELCOME\033[0m')



