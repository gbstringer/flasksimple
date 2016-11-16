import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.forms import NameForm, TitleForm
from app.views import *

bootstrap = Bootstrap()
db = SQLAlchemy()

   
def create_app(config_name):
    tmpl_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
    app = Flask(__name__, template_folder=tmpl_folder)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    db.init_app(app)
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        
        return render_template('index.html', form=form, name=name)
    
    
    
    @app.route('/volnum/<num>')
    def volnum(num):
        return render_template('volnum.html', num=num)
    
    @app.errorhandler(404) 
    def page_not_found(e):
        return render_template('404.html'), 404
      
    return app