from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from info import create_app,db

#调用工厂方法，创建app
app = create_app('dev')

# 创建脚本管理器
manager = Manager(app)

# 迁移时让app和db建立关联
# Migrate(app,db)
# # 把迁移脚本命令添加到脚本管理器对象
# # 'db' 是别名, MigrateCommand 是迁移命令
# manager.add_command('db', MigrateCommand)

@app.route('/', methods = ['GET','POST'])
def index():

    # 测试redis的写入
    # redis_store.set('name','xiaohua')

    # 回顾session缓存保持的数据
    # session['user_id'] = 1
    # session['user_name'] = 'xiaohua'

    return 'index'

# 程序启动入口
if __name__ == '__main__':

    print(app.url_map)
    # app.run()

    manager.run()