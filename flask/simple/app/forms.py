'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, NumberRange


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
class TitleForm(FlaskForm):
    name = StringField('Name of volume: ', validators=[Required()])
    volnum = IntegerField('Volume number: ', validators=[NumberRange(min=1,max=999,message='Please enter a valid volume number')])
    submit = SubmitField('Submit')
    