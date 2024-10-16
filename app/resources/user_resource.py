from flask import Blueprint, jsonify
from app.services import UserService
from app.mapping import UserMap


user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all():
    users = UserService.find_all()
    user_map = UserMap()
    
    return user_map.dumps(users, many=True), 200
    

@user_bp.route('/users/<int:id>', methods=['GET'])
def get(id:int):
    pass
