#!/usr/bin/env python3
'''
Flask app the displays index.html
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashe=False)
def hello_hbnb():
    ''' Returns the index template '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' Main function '''
    app.run()