from flask import flash, jsonify, abort, redirect, render_template, session, url_for
from model.models import Employee, Role, User
from app import app
from config import SECRET_KEY
from flask_login import current_user, login_user
from app.forms import LoginForm

app.secret_key = SECRET_KEY


class Route():
    @app.route("/")
    @app.route('/index')
    def index():
        return "hello world"

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username= form.username.data).filter()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', title='Sign In', form=form)