#!/usr/bin/python3
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    "return states"
    states = []
    states_dec = storage.all(State)
    for st in states_dec.values():
        states.append(st)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(exception):
    "close"
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
