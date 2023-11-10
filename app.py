"""Contains all the routes"""
from flask import Flask
from config import *

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
