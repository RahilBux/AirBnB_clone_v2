#!/usr/bin/python3
"""
Runs an app with flask
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function says hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Function that says HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_comp(text):
    """Displays a message"""
    msg = text.replace('_', ' ')
    return "C %s" % msg


@app.route('/python/')
@app.route('/python/<text>')
def python_comp(text="is_cool"):
    """Displays a message starting with python"""
    msg = text.replace('_', ' ')
    return "Python %s" % msg


@app.route('/number/<int:n>')
def display_int(n):
    """display n only if n is a number"""
    return "%d is a number" % n


@app.route('/number_template/<int:num>')
def num_page(num):
    return render_template('5-number.html', number=num)


@app.route('/number_odd_or_even/<int:num>')
def num_info(num):
    return render_template('6-number_odd_or_even.html', number=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
