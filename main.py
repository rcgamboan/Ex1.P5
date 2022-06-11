from clases import Programa, Traductor, Interprete, actualizar_lista

import sys

#DEFINIR <tipo> [<argumentos>]
    #PROGRAMA <nombre> <lenguaje>
    #INTERPRETE <lenguaje_base> <lenguaje>
    #TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>
#EJECUTABLE <nombre>
#SALIR

print("\nA continuacion introduzca el comando que desee ejecutar:")
print("Los comandos disponibles son:")
print("DEFINIR <tipo> [<argumentos>]")
print("EJECUTABLE <nombre>")
print("SALIR\n")

# Arreglos donde se almacenaran los objetos de cada tipo
# Se emplea un conjunto para guardar que lenguajes pueden ser ejecutados, esto para evitar duplicados

listaProgramas = []
listaInterpretes = []
listaTraductores = []
lenguajesEjecutables = {"LOCAL"}


while True:

    comando = input("main> ")

    argumentos = comando.split()

    if len(argumentos) == 0:
        continue

    #print(argumentos)

    if argumentos[0] in ["SALIR","salir"]:
        print("Se finaliza la ejecucion del programa")
        sys.exit()

    elif argumentos[0] == "DEFINIR":
        
        if argumentos[1] == "PROGRAMA":
            
            if len(argumentos) != 4:
                print("Error en la cantidad de argumentos\n")
                continue
        
            nombre = argumentos[2]
            lenguaje = argumentos[3]

            # Se recorre el arreglo con los programas para ver si el nombre dado ya tiene un programa asociado
            definido = False
            for prog in listaProgramas:
                
                if prog.nombre == nombre:
                    
                    print("El nombre " + nombre + " ya tiene un programa asociado\n")
                    definido = True
                    break
            
            if not definido:
                programa = Programa(nombre,lenguaje)
                listaProgramas.append(programa)
                print("Se ha definido el programa " + nombre + " en el lenguaje " + lenguaje + "\n")
                
            
        elif argumentos[1] == "INTERPRETE":
            
            if len(argumentos) != 4:
                print("Error en la cantidad de argumentos\n")
                continue
            
            base = argumentos[2]
            lenguaje = argumentos[3]
            
            # Se recorre el arreglo con los interpretes para ver si lo solicitado ya se encuentra definido
            definido = False
            for inter in listaInterpretes:

                if inter.lenguajeBase == base and inter.lenguajeInterpretado == lenguaje:
                    print("Ya existe un interprete para el lenguaje " + lenguaje + " escrito en " + base + "\n")
                    definido = True
                    break
            
            if not definido:
                interprete = Interprete(base,lenguaje)
                listaInterpretes.append(interprete)
                print("Se ha definido el interprete de " + lenguaje + " en " + base + "\n")

                if base == "LOCAL" or base in lenguajesEjecutables:
                    lenguajesEjecutables.add(lenguaje)
                


        elif argumentos[1] == "TRADUCTOR":

            if len(argumentos) != 5:
                print("Error en la cantidad de argumentos\n")
                continue

            base = argumentos[2]
            origen = argumentos[3]
            destino = argumentos[4]

            # Se recorre el arreglo con los traductores para ver si lo solicitado ya se encuentra definido
            definido = False
            for trad in listaTraductores:
                if trad.lenguajeBase == base and trad.lenguajeOrigen == origen and trad.lenguajeDestino == destino:
                    print("Ya existe un traductor desde " + lenguaje + " a " + destino + " escrito en " + base + "\n")
                    definido = True
                    break

            if not definido:
                traductor = Traductor(base,origen,destino)
                listaTraductores.append(traductor)
                print("Se ha definido el traductor desde " + traductor.lenguajeOrigen + " a " + traductor.lenguajeDestino + " escrito en " + traductor.lenguajeBase + "\n")
                
                if traductor.lenguajeDestino in lenguajesEjecutables:

                    if traductor.lenguajeBase in lenguajesEjecutables:

                       lenguajesEjecutables.add(traductor.lenguajeOrigen)
                       
    
        
        else:
            print("Error en los argumentos")
            print("Si desea definir un programa por favor siga el siguiente formato:")
            print("DEFINIR PROGRAMA <nombre> <lenguaje>\n")
            print("Si desea definir un interprete por favor siga el siguiente formato:")
            print("DEFINIR INTERPRETE <lenguaje_base> <lenguaje>\n")
            print("Si desea definir un traductor por favor siga el siguiente formato:")
            print("DEFINIR TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>\n")
            

    elif argumentos[0] == "EJECUTABLE":
        
        if len(argumentos) != 2:
            print("Error en los argumentos")
            continue
        
        nombre = argumentos[1]

        definido = False
        for prog in listaProgramas:
            if prog.nombre == nombre:
                definido = True
                programa = prog
                break
        
        if definido:

            if prog.lenguaje not in lenguajesEjecutables:
                lenguajesEjecutables = actualizar_lista(listaInterpretes,listaTraductores,lenguajesEjecutables)
            
            if prog.lenguaje in lenguajesEjecutables:
                print("Es posible ejecutar el programa " + nombre + "\n")
            else:
                print("No se puede ejecutar el programa " + nombre)
                print("Actualmente se pueden ejecutar los siguientes lenguajes : " + str(lenguajesEjecutables) + "\n")
        else:
            print("El programa " + nombre + " no se encuentra definido\n")
            continue

