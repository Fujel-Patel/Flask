from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database.models.BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    posts= relationship(
        "post",
        backref="user",
        cascade= "all, delete_orphan"
    )
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "age": self.age,
            "createdAt": self.createdAt.isoformat(),
        }