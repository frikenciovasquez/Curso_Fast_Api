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
    } 
]
@app.get('/',tags=['home'])

def message():
    return HTMLResponse('<h1> hola mundo </h1>')


@app.get('/movies',tags=['movies'])
def get_movies():
    return movies
