from fastapi import FastAPI,status,HTTPException,APIRouter,Depends
from db import Base,get_db,engine
from sqlalchemy.orm import Session
from src.suppliers.schema import Supplier_Schema
from src.suppliers import controller
from src.auth.security import get_current_user
from src.users.model import User_Model

suppliers_router = APIRouter(prefix="/supplier")

@suppliers_router.post("/create",status_code=status.HTTP_201_CREATED)
def create_supplier(body:list[Supplier_Schema],db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
     return controller.create_supplier(body,db)

@suppliers_router.get("/all_sup",status_code=status.HTTP_200_OK)
def get_all_suppliers(db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
     return controller.get_sup(db)
@suppliers_router.get("/get_by_id/{supplier_id}",status_code = status.HTTP_200_OK)
def get_sup_by_id(supplier_id:int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
     return controller.get_by_id(db,supplier_id)

@suppliers_router.put("/update/{supplier_id}",status_code=status.HTTP_202_ACCEPTED)
def update_sup(supplier_id:int,body:Supplier_Schema,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
     return controller.update_supplier(db,body,supplier_id)
@suppliers_router.delete("/delete/{supplier_id}",status_code=status.HTTP_200_OK)
def delete_sup(supplier_id:int,db: Session = Depends(get_db),current_user: User_Model = Depends(get_current_user)):
     return controller.delete_supplier(db,supplier_id)