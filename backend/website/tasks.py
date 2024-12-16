from flask import Blueprint, render_template, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta, datetime
from .models import Task
from . import db

tasks = Blueprint('tasks', __name__)


@tasks.route('', methods=['GET', 'POST'])
@jwt_required()
def handle_tasks():
    current_user= get_jwt_identity()

    if request.method == 'GET':
        tasks = Task.query.filter_by(user=current_user).all()
        return jsonify([{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status
        } for task in tasks]), 200

    if request.method == 'POST':
        data = request.get_json()
        
        if not data or 'title' not in data:
            return {'error': 'Title is required'}, 400

        new_task = Task(
            title=data['title'],
            description=data['description'],
            user=current_user
        )

        db.session.add(new_task)
        db.session.commit()

        return {
            'id': new_task.id,
            'title': new_task.title,
            'description': new_task.description,
            "user":new_task.user
        }, 201
    

@tasks.route('/<int:task_id>', methods=['PATCH'])
@jwt_required()
def update_task(task_id):
    current_user = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user=current_user).first()
    
    if not task:
        return {'error': 'Task not found'}, 404

    data = request.get_json()

    if 'title' in data:
        task.title = data['title']
    if 'priority' in data:
        task.priority = data['priority']
    if 'status' in data:
        task.status = data['status']
    if 'description' in data:
        task.description = data['description']
    
    task.updated_at = datetime.now()  # Auto-update the time
    
    db.session.commit()
    
    return {
        'id': task.id,
        'title': task.title,
        'priority': task.priority,
        'status': task.status,
        'description': task.description,
        'updated_at': task.updated_at
    }, 200

@tasks.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete(task_id):
    current_user = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user=current_user).first()
    if not task:
        return {"error": "User not found"}, 404
        
    db.session.delete(task)
    db.session.commit()
    return {"message": f"Task {task_id} deleted successfully"}, 200