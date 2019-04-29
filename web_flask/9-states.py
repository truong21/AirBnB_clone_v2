#!/usr/bin/python3
"""
Flask web application that use storage for fetching data from storage engine
"""

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def display_states():
    """ displays a HTML page of states from storage"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    """ display cities objects linked to the State """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def display_states_id(id=None):
    """ display state with list of city when state id is given """
    states = storage.all("State").values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown(exception):
    """ close storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
