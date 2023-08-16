#!/usr/bin/python3
"""Flask Web Application"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """Route for the homepage"""
    return "Hello HBNB!"

@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    """Route for /hbnb"""
    return "HBNB"

@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c_text(text):
    """Route for /c/<text>"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python/", defaults={"text": "is cool"}, methods=['GET'], strict_slashes=False)
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def python_text(text):
    """Route for /python/<text> and /python"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", methods=['GET'], strict_slashes=False)
def number_n(n):
    """Route for /number/<n>"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", methods=['GET'], strict_slashes=False)
def number_template_n(n):
    """Route for /number_template/<n>"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
