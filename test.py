import unittest
from main import definir_interprete, definir_programa, definir_traductor, ejecutable

# para ejecutar las pruebas y calcular la cobertura ejecutar el siguiente comando:
# coverage run -m unittest test.py
# Luego se puede acceder al reporte de la cobertura con el comando
# coverage report
# En el reporte de cobertura se evidencia que la misma es menor al 80%
# Esto se debe a que no se realizan pruebas sobre la funcion imprimir


class Test(unittest.TestCase):

    def test0(self):
        self.assertEqual(definir_programa("factorial","Python") , "Se ha definido el programa factorial en el lenguaje Python\n")
    
    def test1(self):
        self.assertEqual(definir_programa("suma","Java") , "Se ha definido el programa suma en el lenguaje Java\n")
    
    def test2(self):
        self.assertEqual(definir_programa("factorial","Ruby") , "El nombre factorial ya tiene un programa asociado\n")
    
    def test3(self):
        self.assertEqual(definir_programa("fibonacci","Ruby") , "Se ha definido el programa fibonacci en el lenguaje Ruby\n")

    def test4(self):
        self.assertEqual(definir_interprete("LOCAL","Python") , "Se ha definido el interprete de Python escrito en LOCAL\n")
    
    def test5(self):
        self.assertEqual(definir_interprete("LOCAL","Python") , "Ya existe un interprete para el lenguaje Python escrito en LOCAL\n")
    
    def test6(self):
        self.assertEqual(definir_interprete("Python","Ruby") , "Se ha definido el interprete de Ruby escrito en Python\n")
    
    def test7(self):
        self.assertEqual(definir_traductor("Python","C","Ruby") , "Se ha definido el traductor desde C a Ruby escrito en Python\n")
    
    def test8(self):
        self.assertEqual(definir_traductor("Python","C","Ruby") , "Ya existe un traductor desde C a Ruby escrito en Python\n")
    
    def test9(self):
        self.assertEqual(ejecutable("factorial") , "Se puede ejecutar el programa factorial\n")
    
    def testa(self):
        self.assertEqual(ejecutable("fibonacci") , "Se puede ejecutar el programa fibonacci\n")
    
    def testb(self):
        self.assertEqual(ejecutable("suma") , "No se puede ejecutar el programa suma\n")

if __name__ == '__main__':
    unittest.main()
