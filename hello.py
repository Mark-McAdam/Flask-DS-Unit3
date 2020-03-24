from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

# """ Minimal flask app"""

# from flask import Flask

# #make the application
# app = Flask(__name__)

# #make the route
# @app.route("/")

# #define a function for hello world
# def hello():
#     return "Hello World"