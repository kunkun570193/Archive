# coding=utf-8

import logging
import logging.handlers


mylogger = logging.getLogger('post.log')
mylogger.setLevel(logging.DEBUG)
# Add the log message handler to the logger
LOG_FILENAME = 'post.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
            maxBytes=52428800,

            backupCount=1,
           )
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter
mylogger.addHandler(handler)


