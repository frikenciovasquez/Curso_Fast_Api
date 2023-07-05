from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manage import create_token, validate_token
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.user import User


login_router = APIRouter()



@login_router.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password=="admin":
        token: str= create_token(user.dict())
     
        return JSONResponse(status_code=200,content=token) 

