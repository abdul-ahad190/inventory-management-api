from fastapi import FastAPI
from src.products.router import p_router
from db import Base, engine
from src.categories.router import c_router
from src.categories import model
from src.suppliers import model
from src.suppliers.router import suppliers_router
from src.users.router import user_router
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Inventory Management FastAPI")

app.include_router(p_router)
app.include_router(c_router)

app.include_router(suppliers_router)

app.include_router(user_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}