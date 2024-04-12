#!/usr/bin/python3
"""Module to start and manage a Flask web application.

This module creates a Flask web application for displaying a list of states.
It utilizes a teardown context to close database storage after each request,
ensuring proper resource management. States are fetched from a database and
displayed through a dedicated route.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """Close the storage after each request.

    This function is called after each request to close the database connection,
    ensuring all resources are properly freed.

    Args:
        exception (Exception): The exception raised during the request,
                               if any. Defaults to None.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of states on a web page.

    Fetches a list of states from the database and renders them using a
    designated HTML template.

    Returns:
        render_template: The Flask function that renders the template,
                         passing the list of states as a context variable.
    """
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    """Run the Flask application on host 0.0.0.0 and port 5000.

    This allows the application to be accessible over the network.
    """
    app.run(host='0.0.0.0', port=5000)
