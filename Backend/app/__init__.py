
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager

login_manager = LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from model.models import Role, Employee, User, Attendance, Leave, Position
from app.routes import Route

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Role": Role, Employee: "Employee", User: "User",
            Attendance: "Attendance", Leave: "Leave", Position: "Position"}


if __name__ == "__main__":
    app.run(debug=False)
