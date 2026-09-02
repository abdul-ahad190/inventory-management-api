import datetime
from pydantic import BaseModel

class User_Create(BaseModel):
    username: str
    email: str
    password: str

class User_login(BaseModel):
    username: str
    password: str

class User_Response(BaseModel):
    id : int
    username : str
    email : str

class token_response(BaseModel):
    access_token: str
    token_type: str