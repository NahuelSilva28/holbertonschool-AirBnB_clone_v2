#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(x):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           instances=storage.all().values())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
