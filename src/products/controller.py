from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.products.schema import products_create
from src.products.model import Product
from src.categories.model import Category_Model
from src.suppliers.model import Supplier

def post_product(body: products_create, db: Session):
    category = (
        db.query(Category_Model)
        .filter(Category_Model.id == body.category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=400,
            detail=f"Category {body.category_id} does not exist"
        )

    supplier = (
        db.query(Supplier)
        .filter(Supplier.id == body.supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=400,
            detail=f"Supplier {body.supplier_id} does not exist"
        )

    new_product = Product(
        name=body.name,
        price=body.price,
        description=body.description,
        category_id=body.category_id,
        supplier_id=body.supplier_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(body: products_create, product_id: int, db: Session):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    category = db.query(Category_Model).filter(Category_Model.id == body.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail=f"Category {body.category_id} does not exist")

    supplier = db.query(Supplier).filter(Supplier.id == body.supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=400, detail=f"Supplier {body.supplier_id} does not exist")

    existing_product.name = body.name
    existing_product.description = body.description
    existing_product.price = body.price
    existing_product.category_id = body.category_id
    existing_product.supplier_id = body.supplier_id

    db.commit()
    db.refresh(existing_product)
    return existing_product

def delete_product(db: Session, product_id: int):
    existing_product = db.query(Product).filter(Product.id == product_id).first()

    if not existing_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    db.delete(existing_product)
    db.commit()

    return product_id