from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database.models.userModel import User
from extensions import db
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    age = data.get("age")

    if not email or not password or not age:
           return jsonify({
            "success": False,
            "message": "email, password and age are required"
        }), 400

    existingUser = User.query.filter_by(email=email).first()
    if existingUser:
        return jsonify({
            "success": False,
            "message": "User already exists"
        }), 409

    hashed_password = generate_password_hash(password)

    user = User(
        email=email, 
        password=hashed_password,
        age=age
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "User registered successfully"
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "email and password are required"
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({
            "success": False,
            "message": "Invalid credentials"
        }), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "success": True,
        "message": "Login successful",
        "token": access_token
    }), 200


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()  # auth middleware (route protected)
def profile():
    user_id = get_jwt_identity()
    user= User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404
    
    return jsonify({
        "success": True, 
        "user": {
            "id": user.id,
            "email": user.email,
            "age": user.age,
            "createdAt": user.createdAt.isoformat()
        }
    }), 200
