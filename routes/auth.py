from flask import Blueprint, request, jsonify, g
from utils.validator import validate_register
from utils.validator import validate_login
from services.auth_service import create_user
from services.auth_service import login_user
from middlewares.auth_middleware import auth_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    validate_register(data)

    user = create_user(
        email= data["email"],
        password= data["password"],
        age= int(data["age"])
    )

    return jsonify({
        "success": True,
        "message": "user registered successfully",
        "user": user
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    validate_login(data)

    user = login_user(
        email= data["email"],
        password= data["password"]
        )
    return jsonify({
        "success": True,
        "message": "user Login successfully",
        "user": user
    }), 200

@auth_bp.route("/profile", methods=["GET"])
@auth_required   #auth middleware (route protected)
def profile():
    return jsonify({
        "success": True,
        "user": g.user
    })
