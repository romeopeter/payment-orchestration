from app.extensions import db
from datetime import datetime

# ----------------------------------

class User(db.Model):
    """User DB model"""
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)