from fastapi import FastAPI
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
        'category': 'Acción'    
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
        for item in movies:
            if item['category'] == category:
                return item

    
