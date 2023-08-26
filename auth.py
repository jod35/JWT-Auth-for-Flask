from flask import Blueprint, jsonify, request
from models import User

auth_bp = Blueprint('auth',__name__)

@auth_bp.post('/register')
def register_user():

    data = request.get_json()

    user = User.get_user_by_username(username= data.get('username'))

    if user is not None:
        return jsonify({"error":"User already exists"}) , 403
    
    new_user = User(
        username = data.get('username'),
        email = data.get('email')
    )

    new_user.set_password(password= data.get('password'))

    new_user.save()

    return jsonify({"message":"User created"}) , 201