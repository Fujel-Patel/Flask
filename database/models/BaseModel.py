from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from extensions import db

class BaseModel(db.Model):
    __abstract__ = True
    id= Column(Integer, primary_key=True)
    createdAt= Column(DateTime, default= datetime.utcnow)