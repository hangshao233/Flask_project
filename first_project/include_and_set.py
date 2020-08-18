# include 将模板中的语句复用
# set 在模板中定义变量
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("reuse.html")


if __name__ == '__main__':
    app.run(debug=True)
