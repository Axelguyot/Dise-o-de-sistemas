from flask import Blueprint, jsonify


home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje': 'Bienvenido'}), 200