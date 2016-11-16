'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask import Flask

app = Flask(__name)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'



if __name__ == '__main__':
    app.run(debug=True)