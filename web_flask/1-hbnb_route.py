#!/usr/bin/python3
"""
Runs an app with flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Function says hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Function that says HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
