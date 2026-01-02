from flask import jsonify
from utils.exceptions import ValidationError

def register_error_handler(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({"error": e.message}), e.status_code

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "route not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500
