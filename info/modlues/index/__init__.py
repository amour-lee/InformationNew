from flask import Blueprint


# 创建index模块的蓝图
index_blue = Blueprint('index',__name__)

# 保证视图可以被导入
from . import views
