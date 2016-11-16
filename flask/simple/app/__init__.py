import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')
    
def create_app(config_name):
    tmpl_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
    app = Flask(__name__, template_folder=tmpl_folder)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    
    
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
        
    
    
    return app