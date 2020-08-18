
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def macro_import():
    return render_template("macro_import.html")

if __name__ == '__main__':
    app.run(debug=True)