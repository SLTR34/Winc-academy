# Do not modify these lines
__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

# Add your code after this line

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Sweet home!"

@app.route("/greet")
def greet():
    return "Hello World"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

