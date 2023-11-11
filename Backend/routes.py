from app import app
from flask import jsonify
class routes():
    @app.route('/home')
    def index():
        return jsonify(message='Hello world')