
from sqlalchemy import Column, Integer, String
from db import Base


class Category_Model(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
