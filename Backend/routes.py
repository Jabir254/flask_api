from app import app
from flask import jsonify
from model.models import Employee, Role

class routes():
    @app.route('/', methods= ["GET"])
    def index():
        return jsonify(Role.query.get_or_404(id).to_dict())