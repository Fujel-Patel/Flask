from datetime import datetime
from extension import db

class User(db.Model):
    __tablename__ = "user"

    id= db.Column(db.Integer, primary_key= True)
    email= db.Column(db.String(255), unique=True, nullable=False, index= True)
    password= db.Column(db.String(255), nullable= False)
    createdAt= db.Column(db.DateTime, default= datetime.utcnow)