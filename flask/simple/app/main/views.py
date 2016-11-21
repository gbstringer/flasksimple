'''
Created on 17 Nov 2016

@author: gbstring
'''
from flask import render_template, session, redirect, url_for
from . import main
from .forms import TitleForm
from ..models import Title



@main.route('/', methods=['GET', 'POST'])
def index():
    form = TitleForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'))
 
@main.route('/titles', methods=['GET', 'POST'])
def titles():
    form = TitleForm()
    if form.validate_on_submit():
        title = Title(name=form.name.data, author=form.author.data, volnum=form.volnum.data)
        app.db.session.add(title)
        return redirect(url_for('.index'))
    titles = Title.query.order_by(Title.name).all()
    return render_template('titles.html',form=form, titles=titles)