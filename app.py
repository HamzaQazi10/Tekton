from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, Xgrid Learner!'

def create_app():
    return app