import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app
from utils.exceptions import ValidationError

def generate_token(payload):
    exp= datetime.now(timezone.utc) + timedelta(
        minutes= current_app.config["JWT_EXPIRY_MIN"]
    )

    # create token
    token = jwt.encode(
        { **payload, "exp": exp},
        current_app.config["JWT_SECRET"],
        algorithm="HS256"
    )
    return token

def verify_token(token):
    try:
        payload= jwt.decode(
            token,
            current_app.config["JWT_SECRET"],
            algorithms= "HS256"
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValidationError("token expired", 401)
    except jwt.InvalidTokenError:
        raise ValidationError("Invalid token", 401)