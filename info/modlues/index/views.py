from . import index_blue
from flask import render_template


@index_blue.route('/', methods = ['GET','POST'])
def index():

    # 测试redis的写入
    # redis_store.set('name','xiaohua')

    # 回顾session缓存保持的数据
    # session['user_id'] = 1
    # session['user_name'] = 'xiaohua'

    # import logging
    # logging.debug('测试debug')
    # logging.error('测试error')
    # logging.warning('测试warning')
    # logging.fatal('测试fatal')

    return render_template('news/index.html')

