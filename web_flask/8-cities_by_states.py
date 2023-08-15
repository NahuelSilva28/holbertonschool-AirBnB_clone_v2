#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    "Close the session after each Request"
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template("8-cities_by_states.html",
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)