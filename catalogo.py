import json
from satelite import Satelite
from funciones_base import obtener_posicion

def leer_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos_no_procesados=json.load(archivo)
            return datos_no_procesados
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"error en leer el json; {e}")
        return[]
    
def crear_catalogo(datos_no_procesados):
    lista_satelites=[]
    for i in datos_no_procesados:
        try:
            print(f"diccionarios de satelites:", i)
            nombre=i["OBJECT_NAME"]
            numero=i["NORAD_CAT_ID"]
            latitud, longitud, altitud=obtener_posicion(i)
            satelite=Satelite(nombre, numero, latitud, longitud, altitud)
            lista_satelites.append(satelite)
        except ValueError as error:
            nombre_de_sat_invalido=i["OBJECT_NAME"]
            print(f"no se pudo cargar el satelite {nombre_de_sat_invalido}: {error}")
    return lista_satelites


def resumen(satelites):
    tipo_orbitas={"LEO": [], "MEO": [], "GEO": [], "HEO": []}
    for i in satelites:
        tipo=i.tipo_de_orbita()
        if tipo in tipo_orbitas:
            tipo_orbitas[tipo].append(i.altitud)
    estadisticas_de_resultados={}
    for i, e in tipo_orbitas.items():
        cantidad=len(e)
        orbita_min=0
        orbita_max=0
        orbita_pro=0
        if cantidad==0:
            orbita_min=orbita_max=orbita_pro=0.0
        else:
            orbita_min=min(e)
            orbita_max=max(e)
            orbita_pro=sum(e)/cantidad
        estadisticas_de_resultados[i]={"cantidad": cantidad, "Minimo": orbita_min, "Maximo": orbita_max, "Promedio": orbita_pro}
    return estadisticas_de_resultados

def filtro_de_zona(satelites, longitud_minima, latitud_minima, longitud_maxima, latitud_maxima):
    satelites_en_zona=[]
    for i in satelites:
        if i.dentro_de_zona(longitud_minima, latitud_minima, longitud_maxima, latitud_maxima):
            satelites_en_zona.append(i)
    return satelites_en_zona

    
