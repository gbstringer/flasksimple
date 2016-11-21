'''
Created on 21 Nov 2016

@author: gbstring
'''

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

