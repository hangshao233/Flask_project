from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "username": "hangshao",
        "age": -18,     # abs_filter
        "es": "<script>alert('hello');</script>",
        "books": ["Python", "PHP", "Java"],
        "now_time": datetime(2020, 8, 17, 18, 0, 0)
    }
    return render_template("index1.html", **context)

@app.template_filter("handle_time")
def handle_time(time):
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp >= 60 and timestamp <= 60*60:
            return "%s分钟之前" % int(timestamp/60)
        elif timestamp >= 60*60 and timestamp <= 60*60*24:
            return "%小时之前" % int(timestamp/3600)

if __name__ == '__main__':
    app.run(debug=True)