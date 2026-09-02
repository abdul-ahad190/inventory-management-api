from pydantic import  BaseModel

class Supplier_Schema(BaseModel):
    name: str
    address: str
    phone: str
