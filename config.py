import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY","dev-secret")
    JWT_SECRET = os.getenv("JWT_SECRET", "jwt-dev-secret")
    JWT_EXPIRY_MIN = 30