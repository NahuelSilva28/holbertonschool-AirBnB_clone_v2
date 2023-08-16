#!/usr/bin/python3
"""Flask Web Application"""

from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Route for /hbnb
@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"

# Route for /c/<text>
@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))

# Route for /python/<text> and /python
@app.route("/python/", defaults={"text": "is cool"}, methods=['GET'], strict_slashes=False)
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace("_", " "))

# Route for /number/<n>
@app.route("/number/<int:n>", methods=['GET'], strict_slashes=False)
def number_n(n):
    return "{} is a number".format(n)

# Route for /number_template/<n>
@app.route("/number_template/<int:n>", methods=['GET'], strict_slashes=False)
def number_template_n(n):
    return render_template('5-number.html', n=n)

# Route for /number_odd_or_even/<n>
@app.route("/number_odd_or_even/<int:n>", methods=['GET'], strict_slashes=False)
def number_odd_or_even_n(n):
    parity = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
