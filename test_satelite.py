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

def test_limite_de_longuitud():
    assert Satelite("satlon",6,0,0,0).limite_de_longitud()

