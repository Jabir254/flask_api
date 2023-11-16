from flask import jsonify, abort, session
from model.models import Employee, Role
from app import app
from config import SECRET_KEY

app.secret_key = SECRET_KEY


class Route():
    @app.route("/")
    def index():
        return "hello world"

    @app.route("/login", methods=['GET', 'POST'])
    def user():
        pass
