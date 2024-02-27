#!/usr/bin/python3
"""Flask app"""

from flask import Flask
import os
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '5000')
    port = int(os.getenv('HBNB_API_PORT', '0.0.0.0'))
    app.run(host=host, port=port, threaded=True)
