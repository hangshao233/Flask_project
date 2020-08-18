from flask import Flask, url_for, request, redirect, Response
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    print(url_for("article_list", aid=2))
    return "hello world"

@app.route('/article/<aid>/')
def article_list(aid):
    return "article list {}".format(aid)

# 默认接收GET请求
# @app.route('/login/', methods=['GET','POST'])
# def login():
#     # GET请求
#     print(request.args.get("username"))
#     # POST请求
#     print(request.form.get("username"))
#     return "login"

@app.route('/login/')
def login():
    return "login"

@app.route('/profile/')
def profile():
    name = request.args.get("name")
    if name:
        return name
    else:
        # 重定向到登录页面
        # return redirect(url_for("login"))
        return redirect('/login/', code=301) # 默认为302

# 可以返回的数据类型
@app.route('/index_response/')
def index_response():
    # return "hangshao"
    # return {"name":hangshao}
    # return ("hangshao","handsome")
    # return Response("关于hangshao")
    return make_response("关于hangshao")

if __name__ == '__main__':
    app.run(debug=True)