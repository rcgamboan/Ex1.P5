import unittest
from clases import Programa, Traductor, Interprete, actualizar_lista

# para ejecutar las pruebas y calcular la cobertura ejecutar el siguiente comando:
# coverage run -m unittest test.py
# Luego se puede acceder al reporte de la cobertura con el comando
# coverage report
# En el reporte de cobertura se evidencia que la misma es menor al 80%
# Esto se debe a que no se realizan pruebas sobre la funcion imprimir
class TestBuddy(unittest.TestCase):

    def test_asignar_0(self):
        self.assertEqual(buddy.reservar('p0',0) , '\nNo se ha solicitado memoria', "No se debe asignar nada")

        


if __name__ == '__main__':
    unittest.main()
