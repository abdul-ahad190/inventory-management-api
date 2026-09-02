from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from src.categories.schema import Category_Create,respose_category
from db import get_db
from src.categories import controller
from src.auth.security import get_current_user
from src.users.model import User_Model
c_router = APIRouter(prefix="/categories")

@c_router.post("/category", status_code=status.HTTP_201_CREATED,response_model=list[respose_category])
def create_category(
    body: list[Category_Create],
    db: Session = Depends(get_db),
    current_user: User_Model = Depends(get_current_user)
):
    return controller.create_categories(body,db)

@c_router.get("/get_all_categories",status_code=status.HTTP_200_OK,response_model=list[respose_category])
def get_all_categories(db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.get_category(db)


@c_router.get("/categorie/{category_id}",status_code=status.HTTP_200_OK,response_model=respose_category)
def get_by_id(category_id: int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.get_by_id(category_id, db)

@c_router.put("/update_categorie/{category_id}",status_code=status.HTTP_202_ACCEPTED)
def update_category(body:Category_Create,category_id:int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.update_category(body,category_id,db)

@c_router.delete("/delete_categorie/{category_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_category(category_id:int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
    return controller.delete_category(category_id,db)