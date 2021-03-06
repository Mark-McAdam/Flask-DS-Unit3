""" Code for the app
import Flask
make the application
make the routes 
"""
from flask import Flask, render_template, request
from .models import db, User
from decouple import config 



#make app factory - reference the app.py file and the function inside
def create_app():
    app = Flask(__name__)

    # added this to suppress a warning that I was receiving. 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #add config for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    #initialize database for the app - move to postgresql for the final format
    db.init_app(app)


    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home Page', users=users)

    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template('base.html', title = 'RESET TED', users=[])


    return app


# How I manually added tweets from elon musk to the database.
# from TWITOFF.twitter import *
# twitter_user=TWITTER.get_user('elonmusk')
# tweets=twitter_user.timeline(count=200, exclude_replies=True,include_rts=False, tweet_mode='extended')
# db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)


# for tweet in tweets:
# ...     embedding=BASILICA.embed_sentence(tweet.full_text,model='twitter')
# ...     db_tweets = Tweet(id=tweet.id, text=tweet.full_text[:500], user_id=twitter_user.id, embedding=embedding) 
# ...     db.session.add(db_tweets)
# ...     db_user.tweets.append(db_tweets)

# db.session.add(db_user)
# db.session.commit()