#!/usr/bin/python3
"""
Flask application to display a HTML page only if n is an integer
"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ prints Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ prints HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """ prints "C" followed by value of the text var """
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is_cool"):
    """ prints "Python" followed by value of the text var """
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """ prints “n is a number” only if n is an integer """
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    """ display a HTML page only if n is an integer """
    if n % 2 == 0:
        text = "{} is even".format(n)
    else:
        text = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', n=text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
