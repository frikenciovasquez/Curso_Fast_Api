from fastapi import FastAPI, Body

from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "Mi primera aplicacion con FastAPI"

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
@app.get('/',tags=['home'])

def message():
    return HTMLResponse('<h1> hola mundo </h1>')


@app.get('/movies',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}',tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category : str):
        
        return [item for item in movies if item['category'] ==category]
        '''  for item in movies:
            if item['category'] == category:
                return item'''
          
# metodo post:

@app.post('/movies',tags=['movies'])
def create_movies(id: int = Body(),title:str=Body(),overwiew:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
     movies.append({
          "id":id,
          "title":title,
          "overwiew":overwiew,
          "year":year,
          "rating":rating,
          "category":category
          })
     return movies
     
     
@app.put('/movies/{id}',tags=['movies'])
def update_movie(id: int,title:str=Body(),overwiew:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
     for item in movies:
          if item['id']==id:
            item['title']=title,
            item['overwiew']=overwiew,
            item['year']=year,
            item['rating']=rating,
            item['category']=category
            return movies

@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
        for item in movies:
          if item['id']==id:
               movies.remove(item)
               return movies
                 
        
    
