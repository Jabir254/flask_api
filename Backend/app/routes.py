from flask import jsonify, abort
from model.models import Employee, Role
from app import app

class Route():
    @app.route("/")
    def index():
        return"hello world"