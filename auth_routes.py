from flask import Blueprint, request, jsonify
from auth_utils import hash_password, verify_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = create_user(data['email'], hash_password(data['password']))
    return jsonify({'id': user.id}), 201
