from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 创建app实例 __name__决定了如何查找静态文件
app = Flask(__name__)


class Config(object):

    DEBUG = True

    # 配置mysql：指定数据库位置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@mysql@127.0.0.1：3306/information_new'
    # 禁用追踪mysql 因为mysql性能差，如果再去追踪mysql的所有修改 会再次浪费性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 加载app的配置
app.config.from_object(Config)

# 配置mysql
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'

# 程序启动入口
if __name__ == '__main__':

    print(app.url_map)
    app.run()
