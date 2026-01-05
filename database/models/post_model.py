from sqlalchemy import Column, String, Integer, ForeignKey
from database.models.BaseModel import BaseModel
from extensions import db

class Post(BaseModel):
    __tablename__= "posts"

    title= Column(String(255), nullable=False)
    content= Column(String(1000), nullable=False)

    user_id= Column(Integer, ForeignKey("users.id"), nullable=False)
    user= db.relationship("User", backref= "posts")