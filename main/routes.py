from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def hello_world():
    return "<h1>Hello, World! from main</h1>"
