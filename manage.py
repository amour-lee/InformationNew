from flask import Flask


# 创建app实例 __name__决定了如何查找静态文件
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

# 程序启动入口
if __name__ == '__main__':

    print(app.url_map)
    app.run()