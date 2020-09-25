#Practica II -- Edgar Alvarez

#Ejercicio 1 – Realizar un programa que solicite al usuario un número indeterminado de números (mientras se 
# tecleen números que no sean cero). Al salir el programa debe dar en pantalla el total de números 
# dados y la suma de ellos.

numero = 1
cantidad = 0
suma = 0
while numero != 0:
    numero = int(input("Ingreso un numero: "))
    if numero != 0:
        suma = suma + numero
        cantidad = cantidad + 1


print(f"Usted ingresó: {cantidad} numeros y la suma es: {suma}")


#Ejercicio 2- Realizar un programa que presente un menú con las siguientes opciones
#1- Convertir grados a Celsius a Fahrenheit
#2- Convertir dólar a pesos
#3- Convertir metros a pies
#4- Salir
#Cada vez que finalice una de estas acciones debe regresar al menú. El programa solo finalizará cuando el usuario elija la opción salir

x = 0
while x != 4:
    print("1. Convertir grados a Celsius a Fahrenheit")
    print("2. Convertir dólar a pesos")
    print("3. Convertir metros a pies")
    print("4. Salir")
    opcion = int(input("Por favor ingrese la operación deseada: "))

    if opcion == 1:
        celsius = int(input("Intruduzca grados Celsius: "))
        Fahrenheit = (celsius * 9/5) + 32
        print("La cantidad de grados Fahrenheit es: " + str(Fahrenheit))

    elif opcion == 2:
        tasa = 58.5
        dolar = int(input("Introduzca cantidad de dolares: "))
        pesos = (dolar * tasa)
        print("La cantidad de pesos es: " + str(pesos))
    
    elif opcion == 3:
        metros = int(input("Introduzca cantidad de metros: "))
        pies = (metros * 3.28084)
        print("La cantidad de pies es: " + str(pies))

    else:
        print("\nGracias por consultar.\n")

    x = opcion

print("\nHasta luego.\n")

# Ejercicio 3 - Hacer un programa que genere las tablas de multiplicar de los números múltiplos de 5 
# que hay entre 1 y 1000

Multiplo_de = 5
x = 1

while x <= 1000:
    resultado = Multiplo_de * x
    print(f"{x} X {Multiplo_de} = {resultado * x}")
    x += 1


# Ejercicio 4 - Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

top1 = 416220.00
top2 = 624329.00
top3 = 867123.00

sueldo = float(input("ingrese su sueldo mensual:"))

sueldo_anual = sueldo * 12

ISR = 0
ARS = 0
AFP = 0

if sueldo_anual <= top1:
    print("Excenta")
elif sueldo_anual <= top2:
    excedente = sueldo_anual - top1
    ISR = excedente * 0.15
elif sueldo_anual <= top3:
    excedente = sueldo_anual - top2
    ISR = 31216.00 + (excedente * 0.20)
else:
    excedente = sueldo_anual - top3
    ISR = 79776.00 + excedente * 0.25

isr = ISR / 12
afp = sueldo * 0.0287
ars = sueldo * 0.0304

print("ISR: " + str(isr))
print("AFP: " + str(afp))
print("ARS: " + str(ars))

#Ejercicio 5 - Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.


x = 0
while x != 3:
    print("1. Banco ABC")
    print("2. Otro")
    print("3. Salir")
    Bancos = int(input("Seleccione el banco de su preferencia"))

    if Bancos == 1
        

