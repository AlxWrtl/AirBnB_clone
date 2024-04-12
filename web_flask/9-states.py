#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """Close the storage after each request"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """List all the states sorted by name"""
    all_states = sorted(storage.all(State).values(),
                        key=lambda state: state.name)
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a specific state and its cities sorted by name if found"""
    all_states = storage.all(State).values()
    for state in all_states:
        if state.id == id:
            return render_template('9-states.html', selected_state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
