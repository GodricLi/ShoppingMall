# coding:utf-8


import logging
import os


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_ACCOUNT = ('%s\db\\accounts') % BASEDIR


LOG_LEVEL = logging.INFO

LOG_PATH = os.path.join(BASEDIR, 'logs')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TRANSACTION_INTEREST = 0.05
