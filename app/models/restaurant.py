from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")
    products = relationship("Product", back_populates="restaurant")