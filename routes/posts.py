from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models.post_model import Post
from extensions import db

post_bp = Blueprint("posts", __name__)

@post_bp.route("/posts", method=["POST"])
@jwt_required()
def create_post():
    data= request.get_json() or {}

    title= data.get("title")
    content= data.get("content")

    if not title or not content:
        return jsonify({
            "success": False,
            "message": "title and content are required"
        }), 400
    
    user_id= get_jwt_identity()

    post= Post(
        title= title,
        content= content,
        user_id= user_id
    )

    db.session.add(post)
    db.session.commit()

    return jsonify({
        "success": False,
        "message": "title and content are required"
    }), 201
