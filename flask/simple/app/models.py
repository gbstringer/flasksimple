'''
Created on 16 Nov 2016

@author: gbstring
'''
from .__init__ import db

class Title(db.Model):
    __tablename__ = 'titles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    author = db.Column(db.String(127))
    volnum = db.Column(db.Integer)
    
    '''
    def __init__(self, name, author, volnum):
        self.name = name
        self.author = author
        self.volnum = volnum
    '''
    
    def __repr__(self):
        return '<Title %r>' % self.name
    
    