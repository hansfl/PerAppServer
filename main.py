__author__ = 'hansfl'

from flask import Flask, render_template
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dv")
def dv():
    return json.dumps({"x": [0, 1, 2, 3, 4, 5], "y": [0.11, 2.718, 3.1415, 0.22, 2.718/2.0, 3.1415/2.0]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999, debug=True)