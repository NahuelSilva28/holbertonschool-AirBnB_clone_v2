#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    "Remove the current SQLAlchemy session"
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    return render_template("9-states.html",
                           states=storage.all(State).values(),
                           flag=0)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    return render_template("9-states.html", id=id,
                           states=storage.all(State).values(),
                           flag=1)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
