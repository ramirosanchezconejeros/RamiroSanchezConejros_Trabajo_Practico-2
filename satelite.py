class Satelite:
    def __init__(self, nombre, numero, latitud, longitud, altitud):
        self.nombre=nombre 
        self.numero=numero
        self.latitud=latitud
        self.longitud=longitud
        self.altitud=altitud

        self.nombre_extisente()
        self.validar_numero()
        self.limite_de_latitud()
        self.limite_de_longitud()
        self.tipo_de_orbita()


    def tipo_de_orbita(self):
        if self.altitud >=100:
            if self.altitud < 2000:
                return "LEO"
            elif 2000 <= self.altitud < 34000:
                return "MEO" 
            elif 34000<= self.altitud <=37000:
                return "GEO"
            elif self.altitud > 37000:
                return "HEO"
        elif self.altitud < 100:
            raise ValueError("la altitud orbital del satelite debe ser de al menos 100km")
        
    def limite_de_longitud(self):
        if not (-180 <= self.longitud <= 180):
            raise ValueError("la longitud no es valida (debe estar entre -180 y 180)")
        
    def limite_de_latitud(self):
        if not (-90 <= self.latitud <= 90):
            raise ValueError("la latitud no es valida (debe estar entre -90 y 90)")

    def nombre_extisente(self):
        if not self.nombre or not str(self.nombre).strip():
            raise ValueError("el nombre esta vacio")
        
    def validar_numero(self):
        if not type(self.numero)==int:
            raise ValueError("el numero de catalago debe ser un numeor entero")
        
    def dentro_de_zona(self, longitud_minima, latitud_minima, longitud_maxima, latitud_maxima):
        #print(f"Satélite {self.nombre}: lon={self.longitud}, lat={self.latitud} | Límites: X({longitud_minima} a {longitud_maxima}), Y({latitud_minima} a {latitud_maxima})")
        if longitud_minima <= self.longitud <=longitud_maxima and latitud_minima <= self.latitud <=latitud_maxima:
            return True
        else:
            return False

    def mostrar_forma_cadena (self):
        type_orbita=self.tipo_de_orbita()
        return f" {self.nombre} | {self.numero} | {type_orbita} | {self.altitud}km"