import pytest
from satelite import Satelite

def test_creacion_de_satelite_valido():
    satelite_pruba=Satelite("LCS 1", 1965, -10.5, 50.3, 570)
    assert satelite_pruba.nombre=="LCS 1"
    assert satelite_pruba.numero==1965
    assert satelite_pruba.latitud==-10.5
    assert satelite_pruba.longitud==50.3
    assert satelite_pruba.altitud==570
    assert satelite_pruba.tipo_de_orbita()=="LEO"

def test_tipo_de_orbita():
    assert Satelite("satLEO",1,0,0,500).tipo_de_orbita() =="LEO"
    assert Satelite("satMEO", 2, 0, 0, 15000).tipo_de_orbita() == "MEO"
    assert Satelite("satGEO", 3, 0, 0, 35786).tipo_de_orbita() == "GEO"
    assert Satelite("satHEO", 4, 0, 0, 40000).tipo_de_orbita() == "HEO"

def test_de_orbita_invalida():
    with pytest.raises(ValueError):
        Satelite("invalido",5,0,0,99)

def test_limite_de_longuitud_invalida():
    with pytest.raises(ValueError):
        Satelite("satLon",6,0,190,500)

def test_limite_de_latitud_invalida():
    with pytest.raises(ValueError):
        Satelite("satLat",7,95,0,500)

def test_nombre_existente_invalido():
    with pytest.raises(ValueError):
        Satelite("",8,0,0,500)
    with pytest.raises(ValueError):
        Satelite("  ",9,0,0,500)

"""def test_validar_numero_invalido():
    with pytest.raises(ValueError):
        Satelite("satNum","123",0,0,500)"""

"""def test_dentro_de_zona():
    sat=Satelite("satZona",10,-70,-30,500)
    sat2=Satelite("satZona2",11,-50,-20,500)
    assert sat.dentro_de_zona(-76.30, -46.13, -66.30, -35.13) is True
    assert sat2.dentro_de_zona(-76.30, -46.13, -66.30, -35.13) is False"""

"""def test_mostrar_forma_cadena():
    sat=Satelite("satCad",12,0,0,500)
    cadena=sat.mostrar_forma_cadena()
    assert "satCad" in cadena
    assert "12" in cadena
    assert "LEO" in cadena"""