#!/usr/bin/python3
"""Flask app"""

from flask import Flask
from os import getenv
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Close session"""
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', 5000)
    port = getenv('HBNB_API_PORT', '0.0.0.0')
    app.run(host=host, port=int(port), threaded=True)
