# RamiroSanchezConejros_Trabajo_Practico-2
#progamacion I 2026
#carrera: Ingeneria en Telecomunicaiones- Universisdad de Rio Negro

#estructura del proyecto:

El proyecto se encuentra separados por modulos, indicados por la consigna del tp:
    El modulo principal es el 'cunsultar_satelite.py', en este se ejucutran las consultas sobre los satelites, mediante la line de comandos
    El modulo 'catalogo.py' se encarga de leer el json, crear el catalogo, crear las estadisticas de las orbitas mediante la funcion resumen y tambien filtrar los zatelites que se encuentran en la zona indicada.
    El mudulo 'satelite.py' es el que se encarga de la creacion de la calse Satelite, en esta se le asginas los atributos de 'nombre', 'numero', 'latitud', 'longuitud'y 'altitud', ademas de hacerse las validaciones de que tipo de orbita es, o si es una orbita valida, tambien si 'latitud' y 'longuitud' son validas, tambien si el nombre existe, y que el 'numero' sea un numero entero, y por ultimmo se encarga de mostrar los satelites validos en forma de cadena ({nombre}|{numero}|{tipo de orbita}|{altitud}), en caso que el satelite sea invalido nos mostrara un error.
    El modulo de 'funciones.py' se nos a proporcionado mediante el tp, en este se nos proporciona la funcion de obtener la pocicion, que luego usremos en catalogo.py.
    El ultimo modulo son los 'test_satelitepy' y 'test_catalogo.py', es estos se relizaron pruebs unitarias mediantes 'pytest', en esta se buscan tener un 80% de cobertura.

Como ejecutar las consultas y pruebas:
    para ejecutar las consultas de devera poner los sigientes comandos en la barra de cmonados o terminal, en caso de queres consultar por el resumen de devera ejecutar es comando "python consultar_satelite.py satelites.json resumen", mientras que para consultar en zona, se tendra que ejecutar "python consultar_satelite.py satelites.json zona -76.30 -46.13 -66.30 -36.13", siendo los ultimos 4 argumentos las coordenadas en las que se encuentran los zatelites.
    para las pruebas se deveran ejecutar en la terminal, escribiendo el siguientes comandos, 'pytest' para ver las pruebas unitarias, mientras que 'pytest --cov=. --cov-report=HTML' para poder ver el porcenta de cobertura.

El proyecto se encuentra separado por módulos, indicados por la consigna del TP:

    El módulo principal es el consultar_satelite.py: En este se ejecutan las consultas sobre los satélites mediante la línea de comandos.
    El módulo catalogo.py: Se encarga de leer el JSON, crear el catálogo, generar las estadísticas de las órbitas mediante la función resumen, y también filtrar los satélites que se encuentran en la zona indicada.
    El módulo satelite.py: Es el que se encarga de la creación de la clase Satelite. En esta se le asignan los atributos de nombre, número, latitud, longitud y altitud. Además, se realizan las validaciones del tipo de órbita (si es válida), de si la latitud y la longitud son correctas, de si el nombre existe, y de que el número sea un número entero. Por último, se encarga de mostrar los satélites válidos en forma de cadena ({nombre}|{número}|{tipo de órbita}|{altitud}); en caso de que el satelite sea inválido, mostrará un error.
    El módulo funciones.py: Se nos ha proporcionado mediante el TP. En este se incluye la función para obtener la posición, que luego usaremos en catalogo.py.
    Los módulos test_satelite.py y test_catalogo.py: En estos se realizaron pruebas unitarias mediante pytest, buscando obtener un 80% de cobertura.

Cómo ejecutar las consultas y pruebas:
    Para ejecutar las consultas: Se deberán introducir los siguientes comandos en la terminal. En caso de querer consultar el resumen, se deberá ejecutar: "python consultar_satelite.py satelites.json resumen".
    Mientras que para consultar por zona, se tendrá que ejecutar:"python consultar_satelite.py satelites.json zona -76.30 -46.13 -66.30 -36.13" (siendo los últimos 4 argumentos las coordenadas en las que se buscan los satélites).

Para las pruebas: Se deberán ejecutar en la terminal escribiendo los siguientes comandos:
    "pytest" para ver las pruebas unitarias.
    "pytest --cov=. --cov-report=HTML" para poder ver el porcentaje de cobertura.
