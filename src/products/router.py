from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from db import get_db
from src.categories import model
from src.suppliers import model
from src.products.schema import products_create,products_response
from src.products import controller
from src.auth.security import get_current_user
from src.users.model import User_Model
p_router = APIRouter(prefix="/products")


@p_router.post("/create",status_code=status.HTTP_201_CREATED,response_model=products_response)
def create_product(
    body: products_create,
    db: Session = Depends(get_db),
    current_user: User_Model = Depends(get_current_user)
):
    return controller.post_product(body, db)

@p_router.get("/getdata",status_code=status.HTTP_200_OK)
def get_all_products(db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.get_all_products(db)

@p_router.get("/getproduct/{product_id}",status_code=status.HTTP_200_OK)
def get_product_id(product_id: int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.get_product_id(db,product_id)

@p_router.put("/update/{product_id}",status_code=status.HTTP_202_ACCEPTED,response_model=products_response)
def update_product(
    product_id: int,
    body: products_create,
    db: Session = Depends(get_db),
    current_user: User_Model = Depends(get_current_user)
):
    return controller.update_product(body, product_id, db)

@p_router.delete("/delete/{product_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_product(product_id: int,db: Session = Depends(get_db)):
    return controller.delete_product(db, product_id)