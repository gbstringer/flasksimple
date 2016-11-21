'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask import render_template, session, redirect, url_for
from .forms import TitleForm
from .models import Title
from .__init__ import db
from app import app



