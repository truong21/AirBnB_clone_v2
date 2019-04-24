#!/usr/bin/python3
"""
Flask application to display display “n is a number” only if n is an integer
"""


from flask import Flask

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
