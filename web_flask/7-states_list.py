#!/usr/bin/env python3
from flask import Flask, render_template
import os
# from models import *
# from models import storage

# app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def states():
    return render_template('7-states_list.html')

# @app.teardown_appcontext
# def close(exception):
#     storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
