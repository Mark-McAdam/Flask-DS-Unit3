
""" Minimal flask app"""

from flask import Flask, render_template

#make the application
app = Flask(__name__)

#make the route
@app.route("/")

#define a function for hello world
def hello():
    return render_template('home.html')

# make a second route 

@app.route("/about")
def preds():
    return render_template('about.html')


# This also works with the name == main thing
# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()
