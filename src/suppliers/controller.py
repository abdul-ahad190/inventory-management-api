
from fastapi import  FastAPI,HTTPException
from sqlalchemy.orm import Session
from db import engine, Base
from src.suppliers.schema import Supplier_Schema
from src.suppliers.model import Supplier

def create_supplier(body: list[Supplier_Schema], db: Session):
    suppliers = []

    for item in body:
        supplier = Supplier(**item.model_dump())
        suppliers.append(supplier)

    db.add_all(suppliers)
    db.commit()

    for supplier in suppliers:
        db.refresh(supplier)

    return suppliers

def get_sup(db:Session):
    return db.query(Supplier).all()


def get_by_id(db:Session,sup_id:int):
    if not sup_id:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db.query(Supplier).filter(Supplier.id == sup_id).first()

def update_supplier(db:Session,body:Supplier_Schema,sup_id:int):
    existing_sup = db.query(Supplier).filter(Supplier.id == sup_id).first()
    if not existing_sup:
        raise HTTPException(status_code=404, detail="Supplier not found")

    updated_sup = body.model_dump(exclude_unset=True)

    for field, values in updated_sup.items():
        setattr(existing_sup, field, values)

    db.add(existing_sup)
    db.commit()
    db.refresh(existing_sup)
    return existing_sup

def delete_supplier(db: Session, sup_id: int):
    existing_sup = (
        db.query(Supplier)
        .filter(Supplier.id == sup_id)
        .first()
    )

    if not existing_sup:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db.delete(existing_sup)
    db.commit()

    return {"message": "Supplier deleted successfully"}