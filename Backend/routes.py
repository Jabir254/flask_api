from app import app
from flask import jsonify
from model.models import Employee

class routes():
    @app.route('/home')
    def index():
        return jsonify(message='Hello world')