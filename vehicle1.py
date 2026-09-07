#Actividad de POO
#1. diagrama de clases
#Crear un grafico con la clase figura y el atributo largo
#Crear la clase circulo y cuadrado con los metodos calcular area y calcular perimetro.
#2.Programar en python la clases del grafico anterior con sus respectivos atributos y metodos.

class Figura:
    def __init__(self, largo):
        self.largo = largo

class Cuadrado(Figura):
    def calcular_area(self):
        return self.largo ** 2
    
    def calcular_perimetro(self):
        return self.largo * 4

class Circulo(Figura):
    def calcular_area(self):
        return 3.1416 * (self.largo ** 2)
    
    def calcular_perimetro(self):
        return 2 * 3.1416 * self.largo
    
mi_cuadrado = Cuadrado(5)
print("Cuadrado")
print(f"Área del cuadrado: {mi_cuadrado.calcular_area()}")
print(f"Perímetro del cuadrado: {mi_cuadrado.calcular_perimetro()}")

mi_circulo = Circulo(3)
print("Circulo")
print(f"Área del círculo: {mi_circulo.calcular_area()}")
print(f"Perímetro del círculo: {mi_circulo.calcular_perimetro()}")