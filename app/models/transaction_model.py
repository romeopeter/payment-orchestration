from app.extensions import db
from sqlalchemy.dialects.sqlite import JSON
from datetime import datetime

# -------------------------------------------


class Transaction(db.Model):
    db = db.Column(db.Integer, primary_key=True)
    reference = db.Column(
        db.String(64), unique=True, nullable=False
    )  # Unique gateway ref
    amount = db.Column(db.Integer, nullable=False)
    gateway = db.Column(db.String(32), nullable=False)
    status = db.Column(
        db.String(10), nullable=False, unique=False, default="pending"
    )  # pending, failed, "success"
    metadata = db.Column(db.JSON, nullable=True)
    customer_id = db.column(db.Integer, db.Foreign_key("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
