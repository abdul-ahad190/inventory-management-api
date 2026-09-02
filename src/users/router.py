from fastapi import FastAPI,APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from db import get_db
from db import get_db
from src.users.schema import User_login,User_Create,User_Response,token_response
from src.users import controller

user_router = APIRouter(prefix="/users",tags=["users"])

@user_router.post("/create",status_code=status.HTTP_201_CREATED,response_model=User_Response)
def get_new_user(body: User_Create,db: Session = Depends(get_db)):
    return controller.register_user(body,db)
@user_router.post("/login",response_model=token_response,status_code=status.HTTP_200_OK)
def log_in(body:User_login,db: Session = Depends(get_db)):
    return controller.log_in(body,db)

@user_router.get("/all",status_code=status.HTTP_200_OK,response_model=list[User_Response])
def get_all_users(db: Session = Depends(get_db)):
    return controller.get_all_users(db)