from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Cuisine(Base):
    __tablename__ = "cuisines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    spicy_level = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    cuisine_id = Column(Integer, ForeignKey("cuisines.id"))

    category = relationship("Category", back_populates="menu_items")
    cuisine = relationship("Cuisine", back_populates="menu_items")

Category.menu_items = relationship("MenuItem", back_populates="category")
Cuisine.menu_items = relationship("MenuItem", back_populates="cuisine")

