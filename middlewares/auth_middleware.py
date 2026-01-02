from functools import wraps
from flask import request, g
from utils.token import verify_token
from utils.exceptions import ValidationError

def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise ValidationError("Authorization header is missing", 401)

        parts = auth_header.split(" ")
        if len(parts) != 2 or parts[0] != "Bearer":
            raise ValidationError("Invalid Authorization format", 401)

        token = parts[1]

        payload = verify_token(token)
        if not payload:
            raise ValidationError("Invalid or expired token", 401)

        g.user = payload  # GUARANTEED SET

        return fn(*args, **kwargs)
    return wrapper
