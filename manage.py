from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from info import create_app,db

#调用工厂方法，创建app
app = create_app('dev')

# 创建脚本管理器
manager = Manager(app)

# 迁移时让app和db建立关联
Migrate(app,db)
# 把迁移脚本命令添加到脚本管理器对象
# 'db' 是别名, MigrateCommand 是迁移命令
manager.add_command('db', MigrateCommand)
# 程序启动入口

if __name__ == '__main__':

    print(app.url_map)
    # app.run()

    manager.run()