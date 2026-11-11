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