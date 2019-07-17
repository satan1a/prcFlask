"""第一步，导入Flask类
从flask包导入Flask类，这个类表示一个Flask程序
Flask类是Flask的核心类，提供很多与程序相关的属性和方法
"""
from flask import Flask


"""第二步，实例化Flask类
实例化Flask类，得到程序实例 app，后面直接以 实例名.属性/方法 来调用Flask类中的属性和方法
Flask类的构造方法，第一次参数为，当前模块或包的名字，使用特殊变量 __name__ 表示
__name__ 变量由系统根据所处模块来赋予，例如本程序为 app.py， 则该变量值为 app
"""
app = Flask(__name__)


"""第三步，注册路由
注册路由（route），指的是：为函数附加 app.route() 装饰器，并传入URL规则作为参数，即可以让这个URL与函数建立关联
路由负责管理URL和函数之间的映射，这个函数则称为视图函数（view function）
注意：
    1. 这里的URL指相对URL，必须以 ／ 开头，表示根目录
    2. 可以为同一个视图函数绑定多个URL
    3. 可以使用绑定动态URL，使用 <变量名> 的形式表示
    4. 可以使用defaults参数设置URL变量的默认值，这个参数接收字典作为输入，例如 
       @app.route('/greet', defaults={'name': 'World!'})
       @app.route('greet/<name>')
       如果用户访问/greet，则name
"""
@app.route('/')    # .route()装饰器
def hello_world():    # 视图函数
    return 'Hello World ✌'


"""第四步，启动开发服务器
可以使用Pycharm，结合app.run()方法启动
更推荐使用flask run命令（Flask内置一个命令行交互界面，在虚拟环境下的终端内即可以使用flask命令）
"""
if __name__ == '__main__':
    app.run()
