#!/usr/bin/python3
"Starts a Web Application"
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hbnb():
    "Display 'Hello, HBNB!'"
    return "<p>Hello HBNB!</p>"


if __name__ == "__main__":
    """Starts a web app"""
    app.run(debug=True, host="0.0.0.0", port=5000)
