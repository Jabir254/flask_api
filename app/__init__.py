"""Contains all the routes"""
from flask import Flask, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000,)
