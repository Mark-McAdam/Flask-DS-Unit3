""" There is going to be a lot going on with this file.

""" 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Twitter users for analysis"""
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    
class Tweet(db.Model):
    """ Tweets pulled for analysis"""
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.Unicode(280))
