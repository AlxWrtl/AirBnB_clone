#!/usr/bin/python3
""" Start a Flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """close the storage after each requests"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """list all the states"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """list states with id"""
    all_states = storage.all(State).values()
    for state in all_states:
        if state.id == id:
            return render_template('9-states.html', selected_state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
