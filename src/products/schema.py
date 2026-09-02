from pydantic import  BaseModel

class products_create(BaseModel):
    name : str
    description : str
    price : float
    category_id : int
    supplier_id  : int

class products_response(BaseModel):
    id : int
    name : str
    description : str
    price : float
    category_id : int
    supplier_id : int



