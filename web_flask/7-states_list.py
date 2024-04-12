#!/usr/bin/python3
"""Module to start a Flask web application.

This module initializes a Flask web application designed to display a sorted
list of state objects fetched from a storage system. The module includes
routes to handle web requests and a teardown context to manage database
sessions after each request. It uses Flask's rendering capabilities to
display the states in an HTML template.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render an HTML page with a list of all State objects.

    Fetches all State objects from the storage, sorts them by their 'name'
    attribute, and passes them to an HTML template for rendering.

    Returns:
        render_template: The Flask function that renders an HTML template,
                         passing the sorted list of states.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Handle cleanup after each request by closing the storage session.

    This function is called after each request to ensure that the database
    session is properly closed, thereby freeing resources and avoiding
    potential memory leaks.

    Args:
        exception (Exception): The exception that was raised during the
        request, if any. This is handled by Flask internally.
    """
    storage.close()


if __name__ == '__main__':
    """Run the Flask application on host 0.0.0.0 and port 5000.

    This configuration allows the application to be accessible over the
    network,
    making it possible for users to connect to the app from any device within
    the network.
    """
    app.run(host='0.0.0.0', port=5000)
