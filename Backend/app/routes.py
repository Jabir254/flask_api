from app import app
from flask import jsonify, abort
from model.models import Employee, Role

class route():
    @app.route('/role/<int:id>', methods= ["GET"])
    def index(id):
       role= Role.query.all()
       