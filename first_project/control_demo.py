from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    context = {
        "username": "hangshao",
        "books": ["Python", "PHP", "Java"],
        "user": {
            "name": "hangshao",
            "age": 20,
            "school": "WUST"
        }
    }
    return render_template("if-for.html", **context)


if __name__ == '__main__':
    app.run(debug=True)