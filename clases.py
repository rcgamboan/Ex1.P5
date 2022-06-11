#Pregunta 5 Parcial 1 CI3641
#Elaborado por Roberto Gamboa 16-10394

# Creacion de las clases que se usaran en main.py

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

