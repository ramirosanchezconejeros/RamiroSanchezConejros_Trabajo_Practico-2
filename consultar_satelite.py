import sys
from catalogo import leer_json,crear_catalogo, resumen, filtro_de_zona

def main():
    if len(sys.argv)<3:
        print("los argumentos son insuficienters")
        sys.exit(1)
    ruta_archivo=sys.argv[1]
    tipo_consulta=sys.argv[2].lower()
    datos_verdes=leer_json(ruta_archivo)
    satelites=crear_catalogo(datos_verdes)
    
    if tipo_consulta=="resumen":
        print("se mostrata el resumen de las  orbitas")
        resumen_en_consulta=resumen(satelites)
        for i, e in resumen_en_consulta.items():
            print(f"Orbita: {i}")
            print(f"cantida: {e['cantidad']}")
            if e['cantidad']>0:
                print(f"Altitud Minima: {e['Minimo']}")  
                print(f"Altitud Maxima: {e['Maximo']}")
                print(f"Altitud Promedio: {e['Promedio']}")    

    elif tipo_consulta=="zona":
        if len(sys.argv)<7:
            print("se necesistan ingresar las 4 coordenadas: longitud_minima, latitud_minima, longitud_maxima, latitud_maxima")
            sys.exit(1)
        try:
            longitud_minima=float(sys.argv[3])
            latitud_minima=float(sys.argv[4])
            longitud_maxima=float(sys.argv[5])
            latitud_maxima=float(sys.argv[6])
        except ValueError:
            print("los numeros de las coordenadas son invalidos")
            sys.exit(1)
        print(f"satelites en la zona: longitud minima; {longitud_minima}, latitud minima; {latitud_minima}, longitud maxima; {longitud_maxima}, latitud maxima; {latitud_maxima}")
        cantidad_de_satelites_en_zona=filtro_de_zona(satelites, longitud_minima, latitud_minima, longitud_maxima, latitud_maxima)
        print(f"en la zona hay un total de {len(cantidad_de_satelites_en_zona)} satelites")
        for i in cantidad_de_satelites_en_zona:
            print(i.mostrar_forma_cadena())
    else:
        print(f"la consulta es desconosida '{tipo_consulta}', debe usar 'resumen' o ' zona'")
        sys.exit(1)
main()
            
