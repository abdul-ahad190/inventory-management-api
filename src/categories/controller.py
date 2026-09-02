from fastapi import HTTPException, status,Depends
from sqlalchemy.orm import Session
from src.categories.model import Category_Model
from src.categories.schema import Category_Create,respose_category
from db import get_db


def create_categories(body: list[Category_Create], db: Session):
    new_categories = []

    for item in body:
        new_category = Category_Model(
            **item.model_dump(exclude_unset=True),
        )
        db.add(new_category)
        new_categories.append(new_category)
    db.commit()
    for category in new_categories:
        db.refresh(category)
    return new_categories


def get_category(db: Session):
    return db.query(Category_Model).all()

def get_by_id(category_id : int,db: Session):
    return  db.query(Category_Model).filter(Category_Model.id == category_id).first()

def update_category(body:Category_Create,category_id: int,db:Session):
    existing_category = db.query(Category_Model).filter(Category_Model.id == category_id).first()
    if not existing_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category not found")

    updated_ca = body.model_dump(exclude_unset=True)

    for field,values in updated_ca.items():
        setattr(existing_category,field,values)

    db.add(existing_category)
    db.commit()
    db.refresh(existing_category)

    return existing_category


def delete_category(category_id: int,db: Session):
    exist_category = db.query(Category_Model).filter(Category_Model.id == category_id).first()
    if not exist_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category not found")
    db.delete(exist_category)
    db.commit()
    return exist_category