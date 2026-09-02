from sqlalchemy.orm import Session
from fastapi import  FastAPI,HTTPException,status
from sqlalchemy.sql.functions import current_user
from src.users.schema import User_Create,User_login,User_Response,token_response
from src.users.model import User_Model
import jwt
from pwdlib import  PasswordHash
from src.auth.security import decode_access_token
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
if not SECRET_KEY or not ALGORITHM:
    raise HTTPException(
        status_code=400,detail="SECRET_KEY or ALGORITHM not set"
    )

password_hash = PasswordHash.recommended()
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def register_user(body:User_Create,db:Session):
    user_exist = db.query(User_Model).filter(User_Model.username == body.username).first()
    if user_exist:
        raise HTTPException(status_code=400,detail="User already exists")
    user_exist = db.query(User_Model).filter(User_Model.email == body.email).first()
    if user_exist:
        raise HTTPException(status_code=400,detail="Email already exists")
    new_user = User_Model(
        username=body.username,
        email=body.email,
        password_hash=get_password_hash(body.password)
    )
    print(body)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def log_in(body: User_login, db: Session):
    body.model_dump()
    print(body)
    # 1. Find the user
    existing_user = (
        db.query(User_Model)
        .filter(User_Model.username == body.username)
        .first()
    )

    # 2. User does not exist
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # 3. Verify password
    password_correct = verify_password(
        body.password,
        existing_user.password_hash
    )

    # 4. Password is incorrect
    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # 5. Get token expiration time
    expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    expire_time = datetime.now(timezone.utc) + timedelta(
        minutes=expire_minutes
    )

    # 6. Create JWT payload
    payload = {
        "sub": str(existing_user.id),
        "exp": expire_time
    }

    # 7. Create JWT
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    # 8. Return token
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def get_all_users(db: Session):
    return db.query(User_Model).all()