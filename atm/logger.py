# coding:utf-8


import os
import logging
from conf import settings


access_logger = logging.getLogger('access.log')
access_logger.setLevel(settings.LOG_LEVEL)
log_file = os.path.join(settings.LOG_PATH, 'access.log')
fh = logging.FileHandler(log_file)
fh.setLevel(settings.LOG_LEVEL)
formatter = settings.LOG_FORMAT
fh.setFormatter(formatter)
access_logger.addHandler(fh)


transaction_logger = logging.getLogger('transaction.log')
transaction_logger.setLevel(settings.LOG_LEVEL)
log_file = os.path.join(settings.LOG_PATH, 'transaction.log')
fh = logging.FileHandler(log_file)
fh.setLevel(settings.LOG_LEVEL)
formatter = settings.LOG_FORMAT
fh.setFormatter(formatter)
transaction_logger.addHandler(fh)


