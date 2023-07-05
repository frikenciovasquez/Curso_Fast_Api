# Inicio curso basico de Fast API Platzi

#### Documentacion con swagger.
fast api integra una documentacion autogenerada con swagger que explica que va a tener nuestros endpoints 
basandose en los estandares openAPI

dentro del mundo del interneto el protocolo https es aque que se define como el conjunto de metodos de peticion
que indican al navegador que acciones se desea realizar dentro del servidor 

los metodos principales del protocolo https son:
    -post: crear un nuevo recurso
    -put: editar un recurso
    -get : consultar la informacion de un recurso
    -delete :eliminar un recurso.
basicamente podemos hacer un CRUD

#### metodo Get
#parametros de ruta
dentro del parametro del decorador podemos enviar parametros para realizar filtrados, esto junto a una funcion
donde realicemos el filtrados podemos realizar el filrado.

#### parametros query
cuando se especifica en la funcion va a requerir de un parametro pero no en la ruta (decorador/url), fast api
va a detectarlo como un parametro query


#### Metodo post
para el metodo post dentro de la funcion hay que especificar la estrucutra de datos con la cual estemos trabajando
asi mismo para que la respuesta de esta sea un body y no como un parametro query, a los paramtros hay que añadirles que son de clase Body()

#### metodo delete y metodo put
no son muy diferentes, el metodo delete es basicamente buscar pero en lugar de imprimir es borrar
el metodo put es el metodo post pero en luggar de crear nuevops registros actualiza los ya existentes

## creacion de esquemas

la creacion de esquemas, es crear una clase con los el modelo de datos que vamos a usar, medianmte la libreria pydantic el modulo Basemodel()
es el que nos permite esta accion, poder crear un modelo base de datos y pasarlo a las funciones/ metodos como el argumento de como va  ser el modelo
de datos con el cual va a trabajar


## validacion de datos
las validaciones son la manera en la que podemos nostros realizar control sobre el tipo de datos que se ingresan en nuestros formularios
esto mediante la clase Field de pydantic la cual nos permite especificar las condiciones que tienen que cumplir
los datos para que sean validos por nuestro programa, 
otra cualidad que podemos realizar es dentro de nuestros modelo podemos crear esquemas default, asi de esta forma no es necesario 
pasarlo como atributo si no creando una clase dentro del modelo que nos defina este esquema por defecto

### Validacion de parametros

al igual como se realizo con la validacion de los datos, igualmente se puede realizar una validacion
a los parametros query y los parametros de ruta.
la validacion de los parametros de ruta, se realiza importando la libreria propia de fastApi llamada path
esta validacion se realiza pasandole los limites dentro de los id por ejemplo en el metodo get 
al igual que para los parametros de ruta se usa la clase path para los parametros query se importa el modulo Query
y de igual forma se incluye en el parametro de string incluyendo los limites

### tipos de respuesta

aparte de las respuestas de html, fast api nos permite de igualforma otros tipos de respuesta, por ejemplo
    -JsonResponse: esta nos permite enviar el contenido en formato Json al cliente, esta es por defecto
    la respuesta de fastApi

a fastApi podemos especificarle el modelo de respusta que vamos a obtener, esto se realiza especificando en el parametro de la ruta
con la opcion de response_model, en la cual debemos especificarel tipo de respuesta que queremos que sea dada.
        - si queremos que retorne un listado hayu que importar desde typing esta clase  al igual que se hizo con el optional ,
de igual forma a la funcion se debe especificar la salida al igual que se realizo con el 

### Codigo de estados

los codigos de estado nos da la informacion si una peticion se ha ejecutado correctamente o no, estos codigos de estado 
realizan mediante pasando al parametro de ruta mediante el status_code, de igual forma en el JsonResponse utilizando el 
status_code pasandole el codigo que deberia retornar la funcion

### flujos de autenticacion

el flujo de autenticacion es todo el proceso que realizaremos desde la creacion y validacion de tokens a peticion 
del usuario para el acceso a la ruta que esta solicitando, esto se realizara mediante la libreria pyJWT( python Json web token),
    - un token jwt es un objeto de seguridad que se utiliza para autenticar a los usuarios en aplicaciones web y moviles
    - estos tokens se envian al cliente que los utiliza para demostrar su identidad frente a recursos protegidos del servidor
    

# Inicio curso Intermedio Fast API de Platzi

## ORM
 un orm es una libreria que nos permite la manipulacion de la tablas de las bases de datos como si se 
 trataran de objetos en nuestra aplicacion,
    sqlalchemy es una libreria de orm para python que nos facilitara el acceso a base de datos relacional
    mapeando tablas SQL a clases

dentro de  este proceso es mas sano tener una modulacion del proyecto, tener separados los distintos componentes en sus respectivas carpetas para que el proyecto

    para la creacion de la base de datos, la libreria de sqlachemy lo escensial de la libreria a tener en cuenta
    1. create_engime  : es la que nos crea la conexion con la base de datos 
    2. sessionmaker : la session maker crea una sesion para conectarse a la base de datos y enlazarla a la base de datos ( esto mediante el comando bind)
    3. declarative base : esta nos sirve para manipular todas las tablas de la base de datos

    para la creacion de modelos tambien con la libreria de sqlalchemy es importante recalcar que dentro de las importaciones incluir los tipos de datos que tendria nuestros datos,
    la creacion de nuestra modelo de base de datos es en forma de clase( pensandola desde la vista de objetos) nuestra clase con el atributo __tablename__ le dice a sqlalchemy el nombre de la tabla que se va a usar en la base de datos para cada uno de los modelos

 > ya para la creacion de datos en nuestro modelo
los pasos son los siguientes:

1. crear el modelo de sqlalchemy instanciado con nuestros datos.
2. _add_ este objeto es el que añade los datos a nueastra session de base de datos
3. _commit_ realizamos commit a nuestra base de datos .

> consulta de datos, creacion , elminacion y modificacion

    tanto la consulta, modificacion y eliminacion de datos utilizando el modelo ORM no tienen mucha diferencia uno de otro
        1. lo principal es el metodo de creacion (post), donde tener en cuenta que siempre debemos iniciar una sesion con nuestra base de datos, todo esto mediante la classe session(),
            el segundo punto a tener en cuenta es que en este punto los datos los tenemos estructurados, es diferente el modelo de datos que ya teniamos al modelo orm al cual estamos creando nuestros datos, dicho esto (esto hecho en la practica debo investigar si hay mas formas)   basicamente descomprimir el diccionario de datos que tenemos al modelo orm, añadirlos a la session de nuestra base de datos y realizar commit,
        2. para el metodo get para consultar el contenido en nuestra base de datos, siempre creando una sesion de esta, session posee el metodo query, el cual todas las sentencias select generadas por sqlalchemy orm son construidas por el objeto query
        este objeto tiene distintos metodos los cuales nos serviran para delete, metodos como filter tambien sirve para pasos iniciales para el metodo put

        3. para los metodos delete y put o metodos donde se agrega y/o cambia elementos de la base de datos es importante recordar realizar el commit para que los cambios hechos en la session de la base de datos se realicen en la base de datos

> Manejo de Errores y midelwares

Un middleware es una funcion que trabaja con cada peticion antes de que sea procesada por cualquier operacion de ruta especifica, y tambien con cada respuesta antes de devolverla el 

> creacion de routers
 fast api da la posibilidad de dividir la aplicacion en modulos  mediante routers para dividir el codigo en distintos archivos 

> servicios para consulta de datos
    la implementacion de servicios es una practica para separar un poco el codigo de la aplicacion, en resumen atomizar mas el codigo pasi para que sea presentable, y mantenible en el tiempo 