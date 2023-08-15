#!/usr/bin/python3
"""Flask Web Application"""

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """Route for the homepage"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
