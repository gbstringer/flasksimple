'''
Created on 16 Nov 2016

@author: gbstring
'''

from flask import render_template, session, redirect, url_for, current_app
from .forms import TitleForm
from .models import Title
from .__init__ import db




@app.route('/titles', methods=['GET', 'POST'])
def titles():
    form = TitleForm()
    if form.validate_on_submit():
        title = Title(name=form.name.data, volnum=form.volnum.data)
        db.session.add(title)
        return redirect(url_for('.index'))
    titles = Title.query.order_by(Title.name).all()
    return render_template('titles.html',form=form, titles=titles)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
