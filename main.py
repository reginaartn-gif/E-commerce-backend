from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base
import crud
import schemas

#Creating DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Backend")


#The dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
         db.close()


#ROOT
@app.get("/")
def root():
    return {"message": "E-commerce API is running"}


#USERS
@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.email, user.password)


#PRODUCTS
@app.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(
        db,
        product.name,
        product.price,
        product.description,
        product.category_id
    )


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)