from flask import Blueprint

NAME = 'main'
bp = Blueprint(NAME, __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!!!'

@bp.route('/')
def index():
    return 'Pybo index'

