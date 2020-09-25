Practica III --- Edgar Alvarez

#Ejercicio 1- Hacer una función que potencie un número x a la y


X = 9
Y = 4

def potenciar_variable(X,Y):
    a = X ** Y
    return print(a)

potenciar_variable(X, Y)


#Ejercicio 2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre por pantalla
# el número escrito en letras.


def convertir_no_letras():

    numero = float(input("Digite un numero del 1 al 10: "))

    if numero > 10:
        print("Numero invalido")

    elif numero == 1:
        print("uno")

    elif numero == 2:   
        print("dos")
    
    elif numero == 3:   
        print("tres")

    elif numero == 4:   
        print("cuatro")

    elif numero == 5:   
        print("cinco")

    elif numero == 6:   
        print("seis")

    elif numero == 7:   
        print("siete")

    elif numero == 8:   
        print("ocho")

    elif numero == 9:   
        print("nueve")

    elif numero == 10:   
        print("diez")

    print("\nGracias por consultar\n")

convertir_no_letras()


#Ejercicio 3- Hacer una función que reciba un año como argumento y retorne verdadero si es bisiesto.


def año_bisiesto():

    año = float(input("Por favor ingrese un año: "))

    if año % 400 == 0:
        return print("El año ingresado es bisiesto")
    
    elif año % 100 == 0:
        return print("El año ingresado es bisiesto")
    
    elif año % 4 == 0:
        return print("El año ingresado es bisiesto")

    else:
        return print("El año ingresado no es bisieto")

año_bisiesto()


#Ejercicio 4- Crear una función que evalúe dos números y retorne verdadero si ambos números son iguales.


def funcion_igual():
    no1 = float(input("Por favor, ingrese el primer numero: "))
    no2 = float(input("Por favor, ingreses el segundo numero: "))

    if no1 ==  no2:
        return print("Verdadero")

    else:
        return print("Falso")

funcion_igual()


#Ejercicio 5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del 
# producto de dos números de 2 dígitos es 9009 = 91 × 99. Cree una función que  encuentre el palíndromo 
# más grande hecho del producto de dos números de 3 dígitos.


def palindrómo(numero):
    return str(numero) == str(numero)[::-1]

            
def maxpalindromo(numero2, numero1):
    a = 0
    for b in range(numero1, numero2, -1):
        for c in range(numero1, numero2, -1):
            if palindrómo(b * c):
                if b * c > a:
                    a = b * c
    return a 

print(maxpalindromo(101, 303))


#Ejercicio 6- Hacer una función que reciba una cedula como argumento y diga si la cedula es válida o no.


def cedulaRD():
    cedula = input("Por favor ingrese el numero de su cedula: ")

    if len(cedula) == 11:
        print("Cedula Válida")
    
    else:
        print("Cedula Invalida")

cedulaRD()


#Ejercicio 7- Hacer una función que reciba como argumento una lista de elementos numéricos y retorno 
# otra lista con cada elemento de la primera lista duplicados.

def duplicarLista(lista):

    lista = lista
    for i in range(len(lista)):
        print(lista[i] * 2)

duplicarLista([1, 2, 3, 15, 20])


#Ejercicio 8- Hacer una función que reciba un valor iniciar y uno final, y muestre en pantalla las 
# tablas de multiplicar de los números múltiplos de 6 que hay entre el valor inicial y el valor final.

def multiplosDeSeis(vi,vf):
    m = 6

    if vi > vf:
        print ("Error")

    else:  
        while vi <= vf:
            multiplicar = m * vi
            print(f"{m} X {vi} = {multiplicar}")
            vi += 1

multiplosDeSeis(1,50)
