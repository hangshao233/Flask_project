from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 默认从templates目录中查找
    # return render_template("index.html", username="航少", age=20)
    context = {
        "username": "航少",
        "age": 20
    }
    return render_template("index.html", **context)

@app.route('/profile/')
def profile():
    return render_template("profile/user.html")

if __name__ == '__main__':
    app.run(debug=True)