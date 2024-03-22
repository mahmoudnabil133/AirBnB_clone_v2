#!/usr/bin/env python3
"intro to flask"

from flask import Flask, abort
app = Flask('--name--')


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def desplay(text):
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text=None):
    if not text:
        new_text = 'is cool'
    else:
        new_text = text.replace('_', ' ')
    return f'Python {new_text}'



@app.route('/number/<n>', strict_slashes=False)
def number(n):
    try:
        num = int(n)
        return f'{num} is a number'
    except :
        html_content = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <html>
        <head>
            <title>404 Not Found</title>
        </head>
        <body>
            <h1>Not Found</h1>
            <p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>
        </body>
        </html>
        """
        return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
