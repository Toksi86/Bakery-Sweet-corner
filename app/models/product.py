from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class Product(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    category = relationship("Category", back_populates="products")
