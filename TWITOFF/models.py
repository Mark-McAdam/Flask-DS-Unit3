""" There is going to be a lot going on with this file.
""" 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Twitter users for analysis"""
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    newest_tweet_id = db.Column(db.BigInteger)
    def __repr__(self):
        # return f"<User {self.name}"
        return'<Name: {}>'.format(self.name)

class Tweet(db.Model):
    """ Tweets pulled for analysis"""
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.Unicode(300))
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    embedding = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        # return f"<Tweet {self.text}"
        return'<Tweet: {}>'.format(self.text)

