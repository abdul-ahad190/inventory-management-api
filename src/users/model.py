from sqlalchemy import String, Integer, Column, Boolean, DateTime
from db import Base

class User_Model(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String,nullable = False,unique=True)
    email = Column(String,unique=True,nullable = False)
    password_hash = Column(String,nullable = False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime)


