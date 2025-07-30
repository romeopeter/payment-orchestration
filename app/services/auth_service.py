from app.models.user_model import User
from app.extensions import db
from app.utils.security import hash_password, verify_password

# ---------------------------------------------------------


def register_user(email, password):
    """Register user"""

    # User doesn't exist
    if User.query.filter_by(email=email).first():
        return None

    user = User(email=email, password_hash=hash_password(password))
    db.session.add(user)
    db.session.commit()

    return user


def authenticated_user(email, password):
    """authenticate user"""
    user = User.query.filter_by(email=email).first()

    if user and verify_password(password, user.password_hash):
        return user
    return None
