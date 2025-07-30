from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, authenticated_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# -------------------------------------------------------


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    """Register route"""
    data = request.json
    user, error = register_user(data["email"], data["password"])
    if error:
        return jsonify({"error": error, "status": 400})
    return jsonify({"message": "User register", "user": user, "status": 201})


@auth_bp.route("/login", methods=["POST"])
def login():
    """Login route"""
    data = request.json
    user = authenticated_user(data["email"], data["password"])
    if not user:
        return jsonify({"error": "Invalid credentials", "status": 401})
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token, "status": 200})


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def profile():
    """Token(user) identity route"""
    user_id = get_jwt_identity()
    return jsonify({"user_id", user_id})
