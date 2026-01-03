from flask import Flask, request, jsonify
from extensions import db, jwt
from routes.auth import auth_bp
from utils.error_handler import register_error_handler
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()
    app = Flask(__name__)

        # Config
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register error handlers
    register_error_handler(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Routes
    @app.route("/health")
    def health():
        return jsonify({"success": "Flask chal raha hai"})

    @app.route("/search")
    def search():
        name = request.args.get("name")
        age = request.args.get("age")

        return jsonify({
            "name": name,
            "age": age
        })

    @app.route("/user/<username>")
    def user(username):
        return jsonify({
            "user": username
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=False)
