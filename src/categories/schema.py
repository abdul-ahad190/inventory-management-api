from pydantic import  BaseModel

class Category_Create(BaseModel):
    name: str
    description: str


class respose_category(BaseModel):
    id: int
    name: str
    description: str

