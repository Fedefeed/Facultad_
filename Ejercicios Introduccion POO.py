from hashlib import new
from mimetypes import init

'''         Ejercicio1

class Perros():
    def __init__(self):
        self.nombre=input("Ingrese el nombre del perro\n")
        self.edad=int(input("ingrese la edad\n"))
        self.raza=input("Ingrese la raza a la que corresponde\n")
        self.vacunas=input("Presenta vacunas s/n\n")=='s'
        self.collar=input("Tiene collar s/n\n")=='s'
    
    def imprimir(self, n):
        print("\n \t PERRO ",n,"\n")
        print("El perro se llama ",self.nombre,", tiene ",self.edad," años, es de raza ",self.raza,".")
        if self.vacunas:
            print("Tiene vacunas.")
        else:
            print("No tiene vacuanas.")
        if self.collar:
            print("Tambien tiene collar.")
        else:
            print("Tambien no tiene collar.")

perro1=Perros()
perro2=Perros()
perro3=Perros()
perro4=Perros()
perro1.imprimir("Callejero")
perro2.imprimir(2)
perro3.imprimir(3)
perro4.imprimir(4)
'''
'''     Ejercicio2
class Operaciones():
    def __init__(self):
        self.num1=int(input("Ingrese el primer numero:\n"))
        self.num2=int(input("Ingrese el segundo numero:\n"))
    def sumar(self):
        print("--> ",self.num1," + ",self.num2," = ",(self.num1+self.num2))
    def restar(self):
        print("--> ",self.num1," - ",self.num2," = ",(self.num1-self.num2))
    def multiplicar(self):
        print("--> ",self.num1," x ",self.num2," = ",(self.num1*self.num2))
    def dividir(self):
        print("--> ",self.num1," % ",self.num2," = ",(self.num1/self.num2))
    def hacerTodasLasOpercaciones(self):
        self.sumar
        self.restar
        self.dividir
        self.multiplicar
        
calcular=Operaciones()
calcular.hacerTodasLasOpercaciones()
'''
'''     Ejercicio3
class Empleado():
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:\n")
        self.apellido=input("Ingrese su apellido:\n")
        self.sueldo=float(input("Ingrese su sueldo:\n"))
    def imprimir(self):
        if self.sueldo>100000:
            print("--> ",self.apellido," ",self.nombre," tiene un sueldo de $",self.sueldo,".")
            print("Como su sueldo supera los $100000, debera pagar impuestos.")
            print("Sueldo Bruto: $",self.sueldo,"\nInpuesto del 15%.\nSueldo Neto: $",(self.sueldo+self.sueldo*0,15))
        else:
            print("--> ",self.apellido," ",self.nombre," tiene un sueldo de $",self.sueldo)
            print("El empleado esta exento de inpuestos.")

empleado1=Empleado()
empleado1.imprimir()
'''
'''     Ejercicio3'''    
class Vehiculo():
    def __init__(self):
        self.ruedas=int(input("Ingrese la cantidad de ruedas:\n"))
        self.modelo=input("Ingrese el modelo:\n")
    def imprimir(self):
        print("El modelo ",self.modelo,",tiene ",self.ruedas," ruedas.")
class Moto(Vehiculo):
    def __init__(self):
        super().__init__()
        self.apoyaPie=int(input("Ingrese cuantos apoya pies tiene:\n"))
    def imprimir(self):
        super().imprimir()
        print("Tiene ", self.apoyaPie, " apoya pies.")
class Auto(Vehiculo):
    def __init__(self):
        print("\tAuto")
        super().__init__()
        self.puertas=int(input("Ingrese la cantidad de puertas:\n"))
    def imprimir(self):
        super().imprimir()
        print("Tiene ", self.puertas," puertas.")

auto=Auto()
auto.imprimir()
moto=Moto()
moto.imprimir()