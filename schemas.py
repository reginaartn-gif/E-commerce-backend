from pydantic import BaseModel, EmailStr
from typing import Optional


#USER

class UserCreate(BaseModel):
    email:EmailStr
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


#PRODUCT

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    category_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    category_id: int

    class Config:
       from_attributes = True


#CART

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


#ORDER

class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str

    class Config:
       from_attributes = True