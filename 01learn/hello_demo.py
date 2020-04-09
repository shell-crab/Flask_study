# @Time : 2020/4/9 0:33
# @Author : shell-craw
# @File : hello_demo.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run()