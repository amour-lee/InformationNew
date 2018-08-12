from flask import Flask
from flask_session import Session  # Session 和flask里的session不一样
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import Config

# 创建app实例 __name__决定了如何查找静态文件
app = Flask(__name__)

# 加载app的配置
app.config.from_object(Config)

# 配置redis
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)


# 配置mysql
db = SQLAlchemy(app)

# 开启CSRF保护
# 什么情况下代表保护成功：如果用户发送POST，DELETE，PUT...时，没有携带csrf_token或者错误,服务器返回状态码400／403
CSRFProtect(app)

# 配置Session：将flask中的session的数据引导到redis
Session(app)