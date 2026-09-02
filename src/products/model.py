from sqlalchemy import Column, String, ForeignKey, Integer,Float
from db import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))