import pytest
from catalogo import leer_json, crear_catalogo, resumen, filtro_de_zona
from satelite import Satelite

def test_resumen_vacio():
    resumen_vacio=resumen([])
    assert resumen_vacio["LEO"]["cantidad"]==0
    assert resumen_vacio["MEO"]["cantidad"]==0
    assert resumen_vacio["GEO"]["cantidad"]==0
    assert resumen_vacio["HEO"]["cantidad"]==0

def test_resumen_estadisticas():
    sat1=Satelite("satR1",1,0,0,200)
    sat2=Satelite("satR2",2,0,0,150)
    lista=resumen([sat1,sat2])
    estadisticas_LEO=lista["LEO"]
    assert estadisticas_LEO["cantidad"]==2
    assert estadisticas_LEO["orbita_min"]==150
    assert estadisticas_LEO["orbita_max"]==200
    assert estadisticas_LEO["orbita_pro"]==175

def test_filtro_de_zona_dentro():
    sat=Satelite("satEnZona",1,-70,-30,500)
    zona=filtro_de_zona([sat], -76.30, -46.13, -66.30, -36.13)
    assert len(zona)==1

def test_filtro_de_zona_afuera():
    sat=Satelite("satFueraZona",2,-80,-50,500)
    zona=filtro_de_zona([sat], -76.30, -46.13, -66.30, -36.13)
    assert len(zona)==0

def test_crear_catalogo():
    datos_verdes=[ {"OBJECT_NAME": "LCS 1",
  "OBJECT_ID": "1965-034C",
  "EPOCH": "2026-10-14T05:23:16.941696",
  "MEAN_MOTION": 9.89310992,
  "ECCENTRICITY": 0.00109039,
  "INCLINATION": 32.1401,
  "RA_OF_ASC_NODE": 254.3932,
  "ARG_OF_PERICENTER": 186.1791,
  "MEAN_ANOMALY": 173.8573,
  "EPHEMERIS_TYPE": 0,
  "CLASSIFICATION_TYPE": "U",
  "NORAD_CAT_ID": 1361,
  "ELEMENT_SET_NO": 999,
  "REV_AT_EPOCH": 22167,
  "BSTAR": 0.0011283058,
  "MEAN_MOTION_DOT": 1.7e-07,
  "MEAN_MOTION_DDOT": 0}]
    catalogo=crear_catalogo(datos_verdes)
    assert len(catalogo)==1
    assert catalogo[0].nombre =="LCS 1"
    