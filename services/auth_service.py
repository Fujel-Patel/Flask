from flask import jsonify
from utils.exceptions import ValidationError
from utils.token import generate_token

def create_user(email, password, age):
    for user in users:
        if user["email"] == email:
            raise ValidationError("user already exist", 409)

    hashed_password = generate_password_hash(password) 

    new_user = {
        "email": email,
        "password":hashed_password,
        "age": age
    }

    users.append(new_user)
    return {
        "email": email,
        "age": age
    }

def login_user(email, password):
    user = next((u for u in users if u["email"] == email), None)

    if not user:
        raise ValidationError("Invalid credentials", 401)

    if not check_password_hash(user["password"], password):
        raise ValidationError("Invalid credentials", 401)

    token = generate_token({
        "email": user["email"]
    })

    return {
        "email": user["email"],
        "token": token
    }
