from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


# 创建app实例 __name__决定了如何查找静态文件
app = Flask(__name__)


class Config(object):

    DEBUG = True

    # 配置mysql：指定数据库位置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@mysql@127.0.0.1：3306/information_new'
    # 禁用追踪mysql 因为mysql性能差，如果再去追踪mysql的所有修改 会再次浪费性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 数据库配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

# 配置redis
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)

# 加载app的配置
app.config.from_object(Config)

# 配置mysql
db = SQLAlchemy(app)

# 开启CSRF保护
CSRFProtect(app)

@app.route('/')
def index():

    # 测试redis的写入
    redis_store.set('name','xiaohua')

    return 'index'

# 程序启动入口
if __name__ == '__main__':

    print(app.url_map)
    app.run()
