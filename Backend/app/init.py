
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from app.routes import route
from model.models import Role, Employee, User, Attendance, Leave, Position

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Role": Role, Employee: "Employee", User: "User",
            Attendance: "Attendance", Leave: "Leave", Position: "Position"}


if __name__ == "__main__":
    app.run(debug=True)
