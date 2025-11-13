from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    name = Column(String)
    reviews = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    price = Column(Float, default=0.0)
