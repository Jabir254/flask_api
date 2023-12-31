import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(24)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'employee.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False