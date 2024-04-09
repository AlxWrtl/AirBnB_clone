#!/usr/bin/python3
"""Module for setting up a simple Flask web application.

This module utilizes the Flask library to create a basic web application.
It defines routes to return greeting messages, a specific text, dynamic
content based on URL parameters, and a default value for a dynamic route.
The application is configured to run on any interface ('0.0.0.0') and listens
on port 5000.
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
    """Return a custom message with dynamic text from the URL or a default.

    This route demonstrates the use of a default value if no text is
    provided in the URL. It replaces underscores with spaces in the text.

    Args:
        text (str): The text to be included in the message, with underscores
        replaced by spaces. Defaults to "is_cool".

    Returns:
        str: The formatted message "Python " followed by the processed text.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_to_number(n):
    """Return a message indicating that n is a number if n is an integer.

    Args:
        n (int): An integer.

    Returns:
        str: A message stating "n is a number".
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    """Run the Flask web application on host 0.0.0.0 and port 5000."""
    app.run(host='0.0.0.0', port=5001)
