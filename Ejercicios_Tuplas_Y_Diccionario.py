# [] pydroid3
import string
from tokenize import Double

def ejercicio1():
    curso={}
    continuar="s"
    while continuar=="s":
        asignatra=input("Ingrese el nombre de la asignatura: ")
        nota=int(input("Ingrese la nota correspondiente: "))
        curso[asignatra]={nota}
        continuar=input("¿Desea continuar cargando datos? [s/n]")
    print("Listado del curso")
    for x in curso:
        print(x,curso[x])
    
def ejercicio2():
    curso={}
    continuar="s"
    while continuar=="s":
        asignatra=input("Ingrese el nombre de la asignatura: ")
        nota=int(input("Ingrese la nota correspondiente: "))
        curso[asignatra]={nota}
        continuar=input("¿Desea continuar cargando datos? [s/n]")
    continuar=input("¿Desea modificar algun dato? [s/n]")
    bandera=True
    while continuar=="s":
        print("Listado del curso")
        for x in curso:
            print(x,curso[x])
        modificar=input("Ingrese la asigatura que quiea modificar: ")
        for x in curso:
            if modificar==curso.items:
                curso.update(input("Ingrese la nueva nota: "))
                bandera=False
        if bandera:
            print("Esa asignatura no existe.")    
        continuar=input("¿Desea continuar modificando datos? [s/n]")
    print("Listado del curso")
    for x in curso:
        print(x,curso[x])

def ejercicio3():
    usuario={}
    continuar="s"
    while continuar=="s":
        nombre=input("Ingrese el nombre de la persona: ")
        edad=int(input("Ingrese la edad: "))
        direccion=input("Ingrese la direccion: ")
        telefono=int(input("Ingrese el numero de telefono: "))
        usuario[nombre]={edad,direccion,telefono}
        continuar=input("¿Desea continuar cargando datos? [s/n]")
    print("Listado de usuarios")
    for nombre,edad,direccion,telefono in usuario:
        #Revisar salida
        print("El usuario ",nombre," tiene ",edad," , vive en ",direccion," y su numero de telefono es ",telefono)

def ejercicio4():
    listaDic={}
    continuar="s"
    while continuar=="s":
        nombre=input("Ingrese el nombre del producto: ")
        precio=float(input("Ingrese el precio: "))
        listaDic[nombre]={precio}
        continuar=input("¿Desea continuar cargando datos? [s/n]")
        print("Listado de productos")
    for nombre,precio in listaDic.items:
        print("El producto ",nombre,"  --> $",precio)

def ejercicio5():
    cesta = {}
    continuar = True
    while continuar:
        item = input('Introduce un artículo: ')
        precio = float(input('Introduce el precio de ' + item + ': '))
        cesta[item] = precio
        continuar = input('¿Quieres añadir artículos a la lista (S/N)? ') == "s"
    coste = 0
    print('Lista de la compra')
    for item, precio in cesta.items():
        print(item, " ---> $", precio)
        coste += precio
    print('Coste total: ', coste)
    