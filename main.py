from clases import Programa, Interprete, Traductor

listaProgramas = []
listaInterpretes = []
listaTraductores = []
lenguajesEjecutables = {"LOCAL"}

def definir_programa(nombre,lenguaje):
    # Se recorre el arreglo con los programas para ver si el nombre dado ya tiene un programa asociado
    definido = False
    for prog in listaProgramas:
        
        if prog.nombre == nombre:
            string = "El nombre " + nombre + " ya tiene un programa asociado\n"
            print(string)
            return string
    
    if not definido:
        programa = Programa(nombre,lenguaje)
        listaProgramas.append(programa)
        string = "Se ha definido el programa " + nombre + " en el lenguaje " + lenguaje + "\n"
        print(string)
        return string

def definir_interprete(base,lenguaje):
    
    # Se recorre el arreglo con los interpretes para ver si lo solicitado ya se encuentra definido
    definido = False
    for inter in listaInterpretes:

        if inter.lenguajeBase == base and inter.lenguajeInterpretado == lenguaje:
            string = "Ya existe un interprete para el lenguaje " + lenguaje + " escrito en " + base + "\n"
            print(string)
            return string
    
    if not definido:
        interprete = Interprete(base,lenguaje)
        listaInterpretes.append(interprete)
        string = "Se ha definido el interprete de " + lenguaje + " escrito en " + base + "\n"
        print(string)
        actualizar_lista()
        return string

def definir_traductor(base,origen,destino):
    
    # Se recorre el arreglo con los traductores para ver si lo solicitado ya se encuentra definido
    definido = False
    for trad in listaTraductores:
        if trad.lenguajeBase == base and trad.lenguajeOrigen == origen and trad.lenguajeDestino == destino:
            string = "Ya existe un traductor desde " + origen + " a " + destino + " escrito en " + base + "\n"
            print(string)
            return string


    if not definido:
        traductor = Traductor(base,origen,destino)
        listaTraductores.append(traductor)
        string = "Se ha definido el traductor desde " + traductor.lenguajeOrigen + " a " + traductor.lenguajeDestino + " escrito en " + traductor.lenguajeBase + "\n"
        print(string)
        actualizar_lista()
        return string

def ejecutable(nombre):

    definido = False
    for prog in listaProgramas:
        if prog.nombre == nombre:
            definido = True
            programa = prog
            break
    
    if not definido:
        string = "El programa " + nombre + " no se encuentra definido\n"
        print(string)
        return string

    if programa.lenguaje in lenguajesEjecutables:
        string = "Se puede ejecutar el programa " + nombre + "\n"
        print(string)
        return string
    else:
        string = "No se puede ejecutar el programa " + nombre + "\n"
        print(string)
        return string
        #actualizar_lista()
        #return programa.lenguaje in lenguajesEjecutables

def lista_ejecutables():
    return lenguajesEjecutables

def actualizar_lista():

    for inter in listaInterpretes:
        if inter.lenguajeBase in lenguajesEjecutables:
            lenguajesEjecutables.add(inter.lenguajeInterpretado)
    
    for trad in listaTraductores:
        if trad.lenguajeDestino in lenguajesEjecutables:
                    if trad.lenguajeBase in lenguajesEjecutables:
                       lenguajesEjecutables.add(trad.lenguajeOrigen)
    
    return
