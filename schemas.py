from typing import Optional

from pydantic import BaseModel, EmailStr

class CategorySchema(BaseModel):
    id: int
    name: str

class CuisineSchema(BaseModel):
    id: int
    name: str

class MenuItemSchema(BaseModel):
    id: int
    title: str
    description: str
    price: float
    spicy_level: int
    category: CategorySchema
    cuisine: CuisineSchema
