from app import app
from flask import jsonify
from model.models import Employee, Role

class route():
    @app.route('/role/<int:id>', methods= ["GET"])
    def index(id):
       return jsonify(Role.query.get_or_404(id).to_dict())