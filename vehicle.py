class Vehicle:
    def __init__(self,brand, color, plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
        
    def acelerar(self):
        self.speed += 10
        print(f"El {self.brand} acelero a {self.speed} Kmh")
        
    def desacelerar(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0
        print(f"El {self.brand} desacelero a {self.speed} Kmh")
        
#Creacion de los objetos
my_vehicle = Vehicle('Hiunday', 'Black', 'ABC-123')
my_vehicle.acelerar()
my_vehicle.acelerar()

my_vehicle.desacelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()

#Agregar el atributo plate
#Agregar el metodo desacelerar
#subir a git en el mismo mismo repositorio de ayer

