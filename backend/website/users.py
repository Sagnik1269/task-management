from flask import Blueprint, render_template, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from .models import User
from . import db

users = Blueprint('users', __name__)

@users.route('/me', methods=['GET'])
@jwt_required()
def user_info():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(username=current_user_id).first()
    if not user:
        return {"error": "User not found"}, 404

    user_info = {
        "name": user.first_name + " " + user.last_name,
        "username": user.username,
        "email": user.email
    }

    return jsonify(user_info), 200
