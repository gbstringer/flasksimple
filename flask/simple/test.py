'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap

app = Flask(__name__)

''' configure CSRF secret token - should not be stored in svn or git '''
app.config['SECRET_KEY'] = 'sdhsagfrefcxghdvc bvcdhsvfegfdfvregfrem'

bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404) 
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)