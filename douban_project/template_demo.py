# @ Time    : 2020/4/13 20:08
# @ Author  : JuRan

from flask import Flask, render_template

# static_folder=""  修改static 目录位置
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list/")
def list_article():
    return render_template("list.html")


if __name__ == '__main__':
    app.run(debug=True)