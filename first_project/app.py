from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hangshao')
def hello_hangshao():
    return "This is the first page."

@app.route('/list/<int:aid>')
def article_list(aid):
    return "这是第{}篇文章".format(aid)

@app.route('/<any(article, blog):url_path>/')
def item(url_path):
    return url_path

@app.route('/wd')
def baidu():
    return request.args.get("name")

if __name__ == '__main__':
    app.run(debug=True)
