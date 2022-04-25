def ejercicio1():
        print("Hola Mundo")
    
def ejercicio2():
    a=int(input("Ingrese un numero a sumar -> "))
    b=int(input("Ingrese el sugundo numero a sumar -> "))
    print("La suma de " + str(a) + " + " + str(b) + " es igual a: ", (a+b))
    
def ejercicio3():
    a=float(input("Ingrese el valor del producto -> "))
    print("El precio del producto con 21 de IVA es de: ", (a+a*0.21))

def ejercicio4():
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    while(a==b):
        print("Los numeros son iguales, vuelva a intentarlo.")
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
    if a>b:
        print("El numero ", a," es mayor al numero ", b)
    else:
        print("El numero ", b," es mayor al numero ", a)

def ejercicio5():
    a=int(input("Ingrese un numero: "))
    if a>0 and a<10:
            print("El numero ", a," esta entre 0 y 10")
    else:
            print("El numero ", a," no esta entre 0 y 10")

def ejercicio6():
    a=int(input("Ingrese un numero: "))
    if a>11 and a<20:
            print("El numero ", a," esta entre 11 y 20")
    else:
        if a<30 and a>21:
            print("El numero ", a," esta entre 21 y 30")
        else:
            print("El numero ", a, " no esta entre 11 y 20, ni tampoco entre 21 y 30")

def ejercicio7():
    x=1
    while x<100:
        print(x)
        x=x+1

def ejercicio8():
    for x in range(1,10):
        print(x)

def ejercicio9():
    texto="Hola Mundo"
    for x in range(len(texto)):
        print(texto[x])

def ejercicio10():
    for i in range(1,100):
        if i%2==0:
            print(i)
            
def ejercicio11():
    for x in range(0,10):
        print(x)

def ejercicio12():
    for x in range(5,10):
        print(x)

def ejercicio13():
    for x in range(10,0,-1):
        print(x)

def ejercicio14():
    texto="Hola Mundo"
    for x in range(len(texto)):
        print(x)

