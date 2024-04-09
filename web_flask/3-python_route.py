#!/usr/bin/python3
"""Module for setting up a simple Flask web application.

This module utilizes the Flask library to create a basic web application.
It defines routes to return greeting messages, a specific text, and dynamic
content based on URL parameters. The application is configured to run on any
interface ('0.0.0.0') and listens on port 5000.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Define the root route and return a greeting message.

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Define the '/hbnb' route and return a specific message.

    Returns:
        str: The text "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_to_display(text):
    """Return a custom message with dynamic text from the URL.

    Args:
        text (str): The text to be included in the message, with underscores
        replaced by spaces.

    Returns:
        str: The formatted message "C " followed by the processed text.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_to_python(text):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """Run the Flask web application on host 0.0.0.0 and port 5000."""
    app.run(host='0.0.0.0', port=5000)
