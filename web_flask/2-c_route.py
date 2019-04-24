#!/usr/bin/python3
"""
Flask application to display "C" followed by the value of the text variable
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
