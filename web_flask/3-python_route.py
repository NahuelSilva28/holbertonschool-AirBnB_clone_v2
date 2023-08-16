#!/usr/bin/python3
"""Flask Web Application"""

from flask import Flask

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
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
@app.route("/python", methods=['GET'], strict_slashes=False)
def custom_route(text="is cool"):
    """Route for /c/<text> and /python/<text> and /python"""
    return "{} {}".format("C" if "c" in request.url else "Python", text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
