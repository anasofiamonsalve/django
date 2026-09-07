from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, documento, salario): #Constructor de la clase
        self.nombre = nombre #atributo
        self.documento = documento #atributo
        self.salario = salario #atributo
        
        @abstractmethod #metodo abstracto
        def calcular_bonificacion(self):
            pass
        
        def mostrar_informacion(self): #metodo
            print(f"Nombre: {self.nombre}")
            print(f"Documento: {self.documento}")
            print(f"Salario: {self.salario:,0.f}")
            
        def __str__(self): #metodo
            return f"Nombre: {self.nombre} - Documento: {self.documento}"