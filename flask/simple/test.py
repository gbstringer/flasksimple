'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'



if __name__ == '__main__':
    app.run(debug=True)