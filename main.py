from fastapi import FastAPI, Request , HTTPException

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel  #

from utils.jwt_manage import create_token 
from fastapi.security import HTTPBearer
from config.database import engine,base
from middlewares.error_handler import ErrorHandler

from routers.movie import movie_router
from routers.login import login_router

app = FastAPI()
app.title = "Mi primera aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_router)


base.metadata.create_all(bind=engine)






#metodo get 
@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1> hola mundo </h1>')



        