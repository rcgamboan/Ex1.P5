#Pregunta 5 Parcial 1 CI3641
#Elaborado por Roberto Gamboa 16-10394

# Cliente para interactuar con la implementacion realizada

from main import definir_interprete, definir_programa, definir_traductor, ejecutable
from clases import Programa, Traductor, Interprete
import sys

print("\nA continuacion introduzca el comando que desee ejecutar:")
print("Los comandos disponibles son:")
print("DEFINIR <tipo> [<argumentos>]")
print("EJECUTABLE <nombre>")
print("SALIR\n")

while True:

    comando = input("main> ")

    argumentos = comando.split()

    if len(argumentos) == 0:
        continue


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
            definir_programa(nombre,lenguaje)
            
        elif argumentos[1] == "INTERPRETE":
            
            if len(argumentos) != 4:
                print("Error en la cantidad de argumentos\n")
                continue
            
            base = argumentos[2]
            lenguaje = argumentos[3]
            definir_interprete(base,lenguaje)     

        elif argumentos[1] == "TRADUCTOR":

            if len(argumentos) != 5:
                print("Error en la cantidad de argumentos\n")
                continue

            base = argumentos[2]
            origen = argumentos[3]
            destino = argumentos[4]
            definir_traductor(base,origen,destino)                   
    
        
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

        ejecutable(nombre)

