from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from enum import Enum

# Define the Enums for status and priority
class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), default=func.now())
    tasks = db.relationship('Task')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(10000))
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.TODO, nullable=False)
    priority = db.Column(db.Enum(TaskPriority), default=TaskPriority.MEDIUM, nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone = True), default=func.now())
    user = db.Column(db.Integer, db.ForeignKey('user.id')) 