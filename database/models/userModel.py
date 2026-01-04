from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from extensions import db

class User(db.Model):
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

    createdAt = Column(
        DateTime,
        default=datetime.utcnow
    )
