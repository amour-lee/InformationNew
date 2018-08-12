from flask import Flask, session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session # Session 和flask里的session不一样
from config import Config

# 创建app实例 __name__决定了如何查找静态文件
app = Flask(__name__)


# class Config(object):
#
#     DEBUG = True
#
#     # 配置mysql：指定数据库位置
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@mysql@127.0.0.1：3306/information_new'
#     # 禁用追踪mysql 因为mysql性能差，如果再去追踪mysql的所有修改 会再次浪费性能
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # redis 数据库配置
#     REDIS_HOST = '127.0.0.1'
#     REDIS_PORT = 6379
#
#     # 配置秘钥
#     SECRET_KEY = 'agshdjfk'
#
#     # 配置Session：：将flask中的session的数据引导到redis
#     SESSION_TYPE = 'redis'
#     # 配置redis的位置
#     SESSION_REDIS = StrictRedis(host = REDIS_HOST,port= REDIS_PORT)
#     # 使用签名将Session明文转成密文
#     SESSION_USE_SIGNER = True
#     # 设置session有效期: 这里指的是session的扩展操作session时设置的有效期 以秒为单位
#     PERMANENT_SESSION_LIFETIME = 60 * 60 * 24
# 配置redis
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)

# 加载app的配置
app.config.from_object(Config)

# 配置mysql
db = SQLAlchemy(app)

# 开启CSRF保护
# 什么情况下代表保护成功：如果用户发送POST，DELETE，PUT...时，没有携带csrf_token或者错误,服务器返回状态码400／403
CSRFProtect(app)

# 配置Session：将flask中的session的数据引导到redis
Session(app)

# 创建脚本管理器
manager = Manager(app)

# 迁移时让app和db建立关联
Migrate(app,db)
# 把迁移脚本命令添加到脚本管理器对象
# 'db' 是别名, MigrateCommand 是迁移命令
manager.add_command('db', MigrateCommand)

@app.route('/', methods = ['GET','POST'])
def index():

    # 测试redis的写入
    # redis_store.set('name','xiaohua')

    # 回顾session缓存保持的数据
    session['user_id'] = 1
    session['user_name'] = 'xiaohua'

    return 'index'

# 程序启动入口
if __name__ == '__main__':

    print(app.url_map)
    # app.run()

    manager.run()