from flask import jsonify
from utils.exceptions import ValidationError

def validate_register(data):
    if not data:
       raise ValidationError("Json body is missing")

    email = data.get("email")
    password = data.get("password")
    age = data.get("age")

    if (not email) or (not password) or (age is None):
        raise ValidationError("missing fields")

    if len(password) < 6:
        raise ValidationError("password must be 6 character")

    try:
        age= int(age)
    except ValueError:
        raise ValidationError("age must be a number")

    if age < 18:
        raise ValidationError("age must be 18+")
    return None

def validate_login(data):
    if not data:
        raise "Json body is missing"
    
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        raise "missing fields"
    return None