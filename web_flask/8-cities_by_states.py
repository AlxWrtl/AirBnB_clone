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


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display a list of states with cities"""
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=all_states)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
