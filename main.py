from fastapi import FastAPI, Body, Path, Query,Request , HTTPException, Depends

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel , Field
from typing import Optional, List

from jwt_manage import create_token , validate_token
from fastapi.security import HTTPBearer
from config.database import session,engine,base
from Models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = "Mi primera aplicacion con FastAPI"
app.version = "0.0.1"


base.metadata.create_all(bind=engine)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) :
        auth= await super().__call__(request)
        data= validate_token(auth.credentials)
        if data['email']!= "admin@gmail.com":
            raise HTTPException(status_code=403, detail="credenciales erroneas")
    

class User(BaseModel):
     email:str 
     password:str

class Movie(BaseModel):
    id:Optional[int] = None
    title: str = Field(min_length=5,max_length=15)
    overview:str = Field(min_length=15,max_length=50)
    year:int    = Field(le=2022)
    rating:float = Field (gt=0.0 , le=10.0)
    category:str =Field(min_length=5,max_length=15)

    class Config:
         schema_extra={
              "example":{
                   
                   "title": "mi pelicula",
                   "overview":"resumen de la pelicula bla bla bla bla",
                   "year":2020,
                   "rating": 9.8,
                   "category":"accion"
                   
              }
         }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
        {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "Ahora los pitufos estan mas enojados",
        'year': '2023',
        'rating': 6.5,
        'category': 'fantasia'    
    } 
]
#metodo get 
@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1> hola mundo </h1>')

#los tokens
@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password=="admin":
        token: str= create_token(user.dict())
     
        return JSONResponse(status_code=200,content=token) 



# se usa el argumento dependencies=[Depends()] para hacer que se ejecute nuestra clase y asi realizar la validación del token,
#  por lo que ya no se requiere hacer las validaciones dentro de cada metodo HTTP.
@app.get('/movies',tags=['movies'], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies()-> List[Movie]:
    db= session()
    result= db.query(MovieModel).all()

    return JSONResponse(content=jsonable_encoder(result)) # type: ignore

#metodo get con parametros de ruta
@app.get('/movies/{id}',tags=['movies'], response_model=List[Movie])
def get_movie(id: int = Path(ge= 1, le=2000)) -> List[Movie]: 
    db= session()
    result= db.query(MovieModel).filter(MovieModel.id== id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':'no encontrado'})
    return JSONResponse(content=jsonable_encoder(result))
    

@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category : str= Query(min_length=5 , max_length=15))-> List[Movie]:
        db= session()
        result= db.query(MovieModel).filter(MovieModel.category== category).all()
        return JSONResponse(content=jsonable_encoder(result)) # type: ignore
        '''  for item in movies:
            if item['category'] == category:
                return item'''
          
# metodo post:
@app.post('/movies', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    db = session()
    new_movie= MovieModel(**movie.dict())  # esto basicamente descomprime el diccionario 
    db.add(new_movie)
    db.commit()
    return JSONResponse(content={"message": "Se ha registrado la película"}) # type: ignore
     
     
@app.put('/movies/{id}',tags=['movies'],response_model=dict)
def update_movie(id: int,movie:Movie)-> dict: # type: ignore
     db = session()
     result= db.query(MovieModel).filter(MovieModel.id==id).first()
     if not result:
         return JSONResponse(status_code=404 , content={'message':'no encontrado'})
     result.title =movie.title
     result.overview=movie.overview
     result.year=movie.year
     result.rating=movie.rating
     result.category=movie.category
     db.commit()
     return JSONResponse(content={"message":"Actualizado correctamente"}) # type: ignore

@app.delete('/movies/{id}',tags=['movies'], response_model=dict)
def delete_movie(id:int) -> dict: # type: ignore
        db= session()
        result= db.query(MovieModel).filter(MovieModel.id== id).first()
        if not result:
               return JSONResponse(status_code=404, content={'message':'no encontrado'})
        db.delete(result)
        db.commit()
    
        return JSONResponse(content={"message":"Borrado Correctamente"}) # type: ignore
                 
        
 # validacionm de datos
