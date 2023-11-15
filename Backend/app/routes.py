from main import app
from flask import jsonify, abort
from model.models import Employee, Role

@app.route('/')
def index():
    return 'Hello world'