from fastapi import FastAPI, Body, Path, Query

from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel , Field
from typing import Optional, List


app = FastAPI()
app.title = "Mi primera aplicacion con FastAPI"


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
                   "id":1,
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


@app.get('/movies',tags=['movies'], response_model=List[Movie])
def get_movies()-> List[Movie]:
    return JSONResponse(content=movies)

#metodo get con parametros de ruta
@app.get('/movies/{id}',tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge= 1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)
        else:
            return JSONResponse(status_code= 404)
    

@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category : str= Query(min_length=5 , max_length=15))-> List[Movie]:
        data=[item for item in movies if item['category'] ==category]
        return JSONResponse(content=data)
        '''  for item in movies:
            if item['category'] == category:
                return item'''
          
# metodo post:
@app.post('/movies', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"})
     
     
@app.put('/movies/{id}',tags=['movies'],response_model=dict)
def update_movie(id: int,movie:Movie)-> dict:
     for item in movies:
          if item['id']==id:
            item['title']=movie.title
            item['overview']=movie.overview
            item['year']=movie.year
            item['rating']=movie.rating
            item['category']=movie.category
            return JSONResponse(content={"message":"Actualizado correctamente"})

@app.delete('/movies/{id}',tags=['movies'], response_model=dict)
def delete_movie(id:int) -> dict:
        for item in movies:
          if item['id']==id:
               movies.remove(item)
               return JSONResponse(content={"message":"Borrado Correctamente"})
                 
        
 # validacionm de datos
