from fastapi import APIRouter

from fastapi import   Path, Query, Depends

from fastapi.responses import  JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel , Field
from typing import Optional, List

from fastapi.security import HTTPBearer
from config.database import session
from Models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_middleware import JWTBearer
from services.movie import MovieServices
from schemas.movies import Movie

movie_router = APIRouter()



# se usa el argumento dependencies=[Depends()] para hacer que se ejecute nuestra clase y asi realizar la validación del token,
#  por lo que ya no se requiere hacer las validaciones dentro de cada metodo HTTP.
@movie_router.get('/movies',tags=['movies'], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies()-> List[Movie]:
    db= session()
    result=MovieServices(db).get_movies()

    return JSONResponse(content=jsonable_encoder(result)) # type: ignore

#metodo get con parametros de ruta
@movie_router.get('/movies/{id}',tags=['movies'], response_model=List[Movie])
def get_movie(id: int = Path(ge= 1, le=2000)) -> List[Movie]: 
    db= session()
    result= MovieServices(db).get_movies_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'no encontrado'}) # type: ignore
    return JSONResponse(content=jsonable_encoder(result)) # type: ignore
    

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category : str= Query(min_length=5 , max_length=15))-> List[Movie]:
        db= session()
        result= MovieServices(db).get_movies_category(category)
        return JSONResponse(content=jsonable_encoder(result)) # type: ignore
        '''  for item in movies:
            if item['category'] == category:
                return item'''
          
# metodo post:
@movie_router.post('/movies', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    db = session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"}) # type: ignore
     
     
@movie_router.put('/movies/{id}',tags=['movies'],response_model=dict)
def update_movie(id: int,movie:Movie)-> dict: # type: ignore
     db = session()
     result= MovieServices(db).get_movies_id(id)
     if not result:
         return JSONResponse(status_code=404 , content={'message':'no encontrado'}) # type: ignore
     MovieServices(db).update_movie(id,movie)
     
     return JSONResponse(content={"message":"Actualizado correctamente"}) # type: ignore

@movie_router.delete('/movies/{id}',tags=['movies'], response_model=dict)
def delete_movie(id:int) -> dict: # type: ignore
        db= session()
        result= MovieServices(db).get_movies_id(id)
        if not result:
               return JSONResponse(status_code=404, content={'message':'no encontrado'}) # type: ignore
        MovieServices(db).delete_movie(id)
    
        return JSONResponse(content={"message":"Borrado Correctamente"}) # type: ignore
                 
                 