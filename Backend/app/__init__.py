
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'employee.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from model.models import Role, Employee, User, Attendance, Leave, Position

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Role": Role, Employee: "Employee", User: "User",
            Attendance: "Attendance", Leave: "Leave", Position: "Position"}


@app.route('/')
def index():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)
