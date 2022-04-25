import string


def ejercicio1():
    lista=["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
    print(lista)

def ejercicio2():
    lista=["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
    print("Yo estudio ", lista)

def ejercicio3():
    materias=["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
    notas=[]
    for x in range(5):
        print(materias[x])
        a=int(input("Ingrese la nota "))
        notas.append(a)
    for x in range(5):
        print(materias[x], " --> ", notas[x])

def ejercicio4():
    num=[]
    for x in range(5):
        a=int(input("Ingrese los numeros ganadores: "))
        num.append(a)
    num.sort()
    print(num)

def ejercicio5():
    num=[1,2,3,4,5,6,7,8,9,10]
    num.reverse()
    print(num)

def ejercicio6():
    materias=["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
    notas=[]
    i=0
    while i<len(materias):
        print(materias[i])
        a=int(input("Ingrese la nota "))
        if a<6:
            notas.append(a)
            i=i+1
        else:
            materias.pop(i)

    print("----------Materias-----------")
    x=0
    while x<len(materias):
        print(materias[x], " --> ", notas[x])
        x=x+1
    
def ejercicio7():
    abc=list(string.ascii_lowercase)
    print(abc)
    x=1
    while x<len(abc):
        if x%3==0:
            abc.pop(x)
        x=x+1
    print(abc)

def ejercicio8():
    palabra=input("Ingrese una palabra:  ")
    if palabra==palabra[::-1]:
        print("La palabra es palindromo")
    else:
        print("La palabra no es palindromo")
        
def ejercicio9():
    vec=[50,75,46,22,80,65,8]
    mayor=vec[0]
    menor=vec[0]
    for i in range(0,7):
        if vec[i]<menor:
            menor=vec[i]
        if vec[i]>mayor:
            mayor=vec[i]
    print("El precio mayor es: ", mayor, ". /nEl precio menor es: ",menor ,".")
    
def ejercicio10():
    v1=[1,2,3]
    v2=[-1,0,2]
    print("Suponiendo que el cos es de 360°")
    m1=((v1[0])**2+(v1[1])**2+(v1[2])**2)//2
    m2=((v2[0])**2+(v2[1])**2+(v2[2])**2)//2
    print("El producto escalar es de: ",(m1*m2))

def ejercicio11():
    m1=[]
    m2=[]
    suma=[]
    for x in range(0,2):
        for j in range(0,2):
            print("ingrese")
            m1.append(input())
    for x in range(0,2):
        for j in range(0,2):
            print("Ingrese")
            m2.append(input())
    for x in range(0,2):
        for j in range(0,2):
            suma.append(m1[x,j]+m2[x,j])
    print(suma)
def ejercicio12():
    m1=[]
    m2=[]
    mul=[]
    for x in range(0,2):
        for j in range(0,2):
            m1.append(input())
    for x in range(0,2):
        for j in range(0,2):
            m2.append(input())
    for x in range(0,2):
        for j in range(0,2):
            mul[x][j]=(m1[x][j]*m2[x][j])
    print(mul)
