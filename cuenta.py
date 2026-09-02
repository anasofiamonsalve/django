class cuenta:
    def __init__(self, numero, saldo): #constructor
        self.numero = numero
        self.__saldo = saldo

    def depositar(self, cantidad): #Metodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("la cantidad tiene que ser mayor a cero")

    #metodo retirar
    def retirar(self, cantidad):
        if cantidad > 0:
             if cantidad <= self.__saldo:
                self.__saldo -= cantidad
             else:
                 print("fondos faltantes")
        else:
            print("la cantidad debe ser mayor a 0")

    def imprimirsaldo(self):
        print(f"el saldo de la cuenta es {self.numero} y el saldo es {self.__saldo}")


#Creacion del objeto
cuenta1 = cuenta(1111, 1000)
cuenta1.depositar(1000)
print(cuenta1.imprimirsaldo())