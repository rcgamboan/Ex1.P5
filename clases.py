
class Interprete(object):

    def __init__(self,base,lenguaje):
        self.lenguajeBase = base
        self.lenguajeInterpretado = lenguaje
        
    

class Programa(object):

    def __init__(self,nombre,lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Traductor(object):

    def __init__(self,base,origen,destino):
        self.lenguajeBase = base
        self.lenguajeOrigen = origen
        self.lenguajeDestino = destino

