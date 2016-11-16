'''
Created on 16 Nov 2016

@author: gbstring
'''
from app import db

class Title(db.Model):
    __tablename__ = 'titles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    volno = db.Column(db.Integer)
    def __repr__(self):
        return '<Title %r>' % self.name
    
    