import os
from sqlalchemy import create_engine 
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # este funciona para manipular todas las bases de datos de mis tablas
sqlite_file_name=  "../database.sqlite"

base_dir = os.path.dirname(os.path.realpath(__file__))

database_url= f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine= create_engine(database_url,echo=True)

#Se crea session para conectarse a la base de datos, se enlaza con el comando “bind” y se iguala a engine
session = sessionmaker(bind=engine)

#Sirve para manipular todas las tablas de la base de datos
base = declarative_base() 