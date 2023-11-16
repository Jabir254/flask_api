from flask import jsonify, abort, redirect, session, url_for
from model.models import Employee, Role, User
from app import app
from config import SECRET_KEY
from flask_login import current_user, login_user
from forms import LoginForm

app.secret_key = SECRET_KEY


class Route():
    @app.route("/")
    def index():
        return "hello world"

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()

