from flask import Blueprint, render_template, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from .models import User
from . import db
import bcrypt


auth = Blueprint('auth', __name__)


# /auth/login POST request
# username, password
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return {"error": "No data provided"}, 400
        
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return {"error": "Missing username or password"}, 400
        
    # Find user by username
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"error": "User not found"}, 404

    # Verify password
    if not bcrypt.checkpw(password.encode('utf-8'), user.password):
        return {"error": "Invalid password"}, 401

    # Create token with additional claims
    additional_claims = {
        'username': user.username,
        'email': user.email
    }
    
    access_token = create_access_token(
        identity=user.username,
        expires_delta=timedelta(hours=1),
        # additional_claims=additional_claims
    )

    response = make_response(jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        },
        "access_token": access_token

    }))

    # Set JWT token in HTTP-only cookie
    response.set_cookie("access_token", access_token)

    return response, 200

# /auth/register POST request
# username, password, email, first_name, last_name
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data:
        return {"error": "No data provided"}, 400
        
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not username or not password or not email or not first_name or not last_name:
        return {"error": "Missing field/s"}, 400

    # Check if username exists
    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 409

    # Check if email exists
    if User.query.filter_by(email=email).first():
        return {"error": "Email already exists"}, 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, email=email, first_name=first_name, last_name=last_name, password=hashed_password)

    access_token = create_access_token(
        identity=new_user.username,
        expires_delta=timedelta(hours=1)
    )

    db.session.add(new_user)
    db.session.commit()

    response = make_response(jsonify({"message": "User registered successfully", "username": username, "access_token": access_token}))

    response.set_cookie("access_token", access_token)

    return response, 201


@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    current_user_id = get_jwt_identity()
    
    # Verify the user exists
    user = User.query.get(current_user_id)
    if not user:
        return {"error": "User not found"}, 404

    response = jsonify({"message": "Successfully logged out"})
    
    # Delete the cookie by setting its expiry to past
    response.set_cookie(
        'access_token', '', 
        expires=0,
    )

    return response, 200

@auth.route('/set_cookie', methods=['POST'])
def cookie():
    res = make_response(jsonify({"message": "Successfully logged out"}))
    res.set_cookie("theme", "dark")
    res.set_cookie("mycookie", "coeeekiss")
    return res, 200


@auth.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
        
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User {user_id} deleted successfully"}, 200