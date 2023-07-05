from pydantic import BaseModel , Field
from typing import Optional, List


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
