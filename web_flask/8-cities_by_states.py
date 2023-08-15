#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(x):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template("8-cities_by_states.html",
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
