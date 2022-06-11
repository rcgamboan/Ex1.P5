#Pregunta 5 Parcial 1 CI3641
#Elaborado por Roberto Gamboa 16-10394

# Implementacion de las funciones que permiten definir programas, interpretes y traductores
# Ademas la funcion que permite identificar si algun programa se puede ejecutar

from clases import Programa, Interprete, Traductor

# Arreglos donde se almacenaran los objetos de cada tipo
# Se emplea un conjunto para guardar que lenguajes pueden ser ejecutados, esto para evitar duplicados
# la lista lenguajesEjecutables siempre contiene el lenguaje LOCAL, que la maquina puede entender
listaProgramas = []
listaInterpretes = []
listaTraductores = []
lenguajesEjecutables = {"LOCAL"}

# Funcion que recibe el nombre y lenguaje del  programa que se quiere definir
# Se verifica si el nombre ya se encuentra asociado a algun programa
# Caso contrario se crea un objeto Programa con los datos suministrados
# el objeto luego se agrega a listaProgramas
def definir_programa(nombre,lenguaje):
    
    # Se recorre el arreglo con los programas para ver si el nombre dado ya tiene un programa asociado
    definido = False
    for prog in listaProgramas:
        
        if prog.nombre == nombre:
            string = "El nombre " + nombre + " ya tiene un programa asociado\n"
            print(string)
            return string
    # Si no esta definido, se define y se agrega a la lista
    if not definido:
        programa = Programa(nombre,lenguaje)
        listaProgramas.append(programa)
        string = "Se ha definido el programa " + nombre + " en el lenguaje " + lenguaje + "\n"
        print(string)
        return string

# Funcion que recibe el lenguaje base y lenguaje a interpretar del interprete que se quiere definir
# Se verifica si ya se ha creado un interprete con las caracteristicas indicadas
# Caso contrario se crea un objeto Interprete con los datos suministrados
# el objeto luego se agrega a listaInterpetes
def definir_interprete(base,lenguaje):
    
    # Se recorre el arreglo con los interpretes para ver si lo solicitado ya se encuentra definido
    definido = False
    for inter in listaInterpretes:

        if inter.lenguajeBase == base and inter.lenguajeInterpretado == lenguaje:
            string = "Ya existe un interprete para el lenguaje " + lenguaje + " escrito en " + base + "\n"
            print(string)
            return string
    # Si no esta definido, se define y se agrega a la lista
    if not definido:
        interprete = Interprete(base,lenguaje)
        listaInterpretes.append(interprete)
        string = "Se ha definido el interprete de " + lenguaje + " escrito en " + base + "\n"
        print(string)
        actualizar_lista()
        return string

# Funcion que recibe el lenguaje donde esta escrito, lenguaje de origen y lenguaje destino
# del traductor que se quiere definir
# Se verifica si ya se ha creado un traductor con las caracteristicas indicadas
# Caso contrario se crea un objeto Traductor con los datos suministrados
# el objeto luego se agrega a listaTraductor
def definir_traductor(base,origen,destino):
    
    # Se recorre el arreglo con los traductores para ver si lo solicitado ya se encuentra definido
    definido = False
    for trad in listaTraductores:
        if trad.lenguajeBase == base and trad.lenguajeOrigen == origen and trad.lenguajeDestino == destino:
            string = "Ya existe un traductor desde " + origen + " a " + destino + " escrito en " + base + "\n"
            print(string)
            return string

    # Si no esta definido, se define y se agrega a la lista
    if not definido:
        traductor = Traductor(base,origen,destino)
        listaTraductores.append(traductor)
        string = "Se ha definido el traductor desde " + traductor.lenguajeOrigen + " a " + traductor.lenguajeDestino + " escrito en " + traductor.lenguajeBase + "\n"
        print(string)
        actualizar_lista()
        return string

# Verifica si el programa con el nombre dado existe y si se puede ejecutar
# Para saber si se puede ejecutar, se revisa la lista lenguajesEjecutables
# Dicha lista lleva registro de que lenguajes se pueden ejecutar segun los interpretes y traductores definidos hasta el momento
def ejecutable(nombre):

    # Se verifica si existe el programa
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

# Funcion que revisa los interpretes y traductores creados hasta el momento
# Para cada interprete, se verifica si el lenguaje base se encuentra en la lista lenguajesEjecutables
# Si se encuentra, se agrega el lenguaje interpretado a la lista
# Para cada traductor, se verifica si el lenguaje en el que esta escrito
# y el lenguaje destino se encuentran en la lista lenguajesEjecutables
# de encontrarse, se agrega el lenguaje de origen a la lista
def actualizar_lista():

    for inter in listaInterpretes:
        if inter.lenguajeBase in lenguajesEjecutables:
            lenguajesEjecutables.add(inter.lenguajeInterpretado)
    
    for trad in listaTraductores:
        if trad.lenguajeDestino in lenguajesEjecutables:
                    if trad.lenguajeBase in lenguajesEjecutables:
                       lenguajesEjecutables.add(trad.lenguajeOrigen)
    
    return
