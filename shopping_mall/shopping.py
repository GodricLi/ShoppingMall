# coding:utf-8


from atm import db_handler, logger


def shopping(account):
    """购物商城"""
    data = db_handler.load_account(account)
    goods = [
                {"name": "电脑", "price": 9999},
                {"name": "鼠标", "price": 666},
                {"name": "游艇", "price": 22222},
                {"name": "美女", "price": 998}
                                                    ]
    while True:
        print('\033[32;1mSHOPPING MALL\033[0m'.center(50, '-'))
        for index, i in enumerate(goods):
            print('\033[32;1m%s:%s:%s\033[0m' % (index, i['name'], i['price']))
        print('\033[32;1mEND\033[0m'.center(50, '-'))
        choice = input('输入商品编号选择商品:').strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(goods):
                if goods[choice]['price'] <= data['quota']:
                    data['quota'] -= goods[choice]['price']
                    data['car'].append(goods[choice])
                    print('商品已加入购物车:', data['car'], '\033[32;1m''余额:', data['quota'], '\033[0m')
                else:
                    print('\033[32;1m余额不足,请购买其他商品或退出\033[0m')
        elif choice == 'exit':
            if 0 < len(data['car']):
                db_handler.save_db(data)
                logger.transaction_logger.info('账户-%s购买商品%s' % (account, data['car']))
                exit('bye')