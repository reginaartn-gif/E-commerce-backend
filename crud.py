from sqlalchemy.orm import Session
from models import User, Product, Category, CartItem, Order
import models
import schemas
from auth import hash_password


#USERS

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.User(
       email=user.email,
       password_hash=hashed_password,
       role="user"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


#PRODUCTS

def create_product(db: Session, name: str, price: float, description: str, category_id: int):
    product = Product(
        name=name,
        price=price,
        description=description,
        category_id=category_id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session):
    return db.query(Product).all()


#CART

def add_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
    item = CartItem(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


#ORDERS

def create_order(db: Session, user_id: int, status: str = "pending"):
    order = Order(
        user_id=user_id,
        status=status
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
