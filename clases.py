
class Interprete(object):

    def __init__(self,base,lenguaje) -> None:
        self.lenguajeInterpretado = lenguaje
        self.lenguajeBase = base
    

class Programa(object):

    def __init__(self,nombre,lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Traductor(object):

    def __init__(self,base,origen,destino) -> None:
        self.lenguajeBase = base
        self.lenguajeOrigen = origen
        self.lenguajeDestino = destino

def actualizar_lista(interpretes,traductores,ejecutables):

    for inter in interpretes:
        if inter.lenguajeBase in ejecutables:
            ejecutables.add(inter.lenguajeInterpretado)
    
    for trad in traductores:
        if trad.lenguajeDestino in ejecutables:
                    if trad.lenguajeBase in ejecutables:
                       ejecutables.add(trad.lenguajeOrigen)
    
    return ejecutables