from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)


from model import models
from routes import routes

if __name__ == "__main__":
    app.run(debug=True)
