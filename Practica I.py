# Practica I: Escribir un progrma que...
#1 Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2


expresion1 = 4<2
print(type(expresion1))


#2 Almacene en una variable el nombre de una persona y al final...


Nombre = "pythonators" 
print("Bienvenido: " + (Nombre))


#3 Evalúe si un número es par o impar y muestre en la consola el mensaje


numero = input("ingreso numero: ")
numero = int(numero)
if numero % 2 == 0:
    print("par") 
else:
    print("impar")  


#4 Almacene dos números y evalúe si el primero es mayor que el segundo...


n1 = 7
n2 = 13
print(n1>n2)


#5 Convierta dólares a pesos


cantidad_dolar = input("Ingrese cantidad de dolares: ")
cantidad_dolar = float(cantidad_dolar)
tasa_dolar = 58.5
print(cantidad_dolar*tasa_dolar)


#6 Convierta grados celsius a Fahrenheit


grados_celsius = input("Ingrese grados en celsius: ")
grados_celsius = float(grados_celsius)

def celsius_a_fahrenheit(grados_celsius):

    
    return (grados_celsius * 9.0/5.0) + 32


print(celsius_a_fahrenheit(grados_celsius))


#7 Almacene cuatro notas 90,95,77,92 y las promedie. Al final debe decir...


nota1 = 90
nota2 = 95
nota3 = 77
nota4 = 92
suma = nota1+nota2+nota3+nota4
promedio = suma/4
promedio = int(promedio)

if promedio>=90:
    print("A")
elif promedio<=89>=80:
    print("B")
elif promedio<=79>=70:
    print("C")
elif promedio<=69>=60:
    print("D")
else: 
    promedio<=59
    print("F")


#8 Que almacene monto, cantidad de cuotas, y porcentaje de interés anual

# monto = int(750000)
# cuotas = int(24)
# interes_anual = int(0.16/100.00)
# print(interes_anual)
# interes_anual = int(interes_anual/12)
# print(interes_anual)


# # def valor_de_cuota(monto, interes_anual, cuotas):
# #         return monto * [(interes_anual * ((1 + interes_anual)**cuotas)) / (((1 + interes_anual)**cuotas) - 1)]


# # print(int(valor_de_cuota(monto,interes_anual,cuotas)))


# def valor_de_cuota(monto, interes_anual, cuotas):
#     x = (1 + interes_anual) ** cuotas
#     return monto * (interes_anual * x) / (x - 1)
    

# print(int(valor_de_cuota(monto,interes_anual,cuotas)))



# def valor_de_cuota(monto, interes_anual, años):
#     n=años * 12
#     r=(interes_anual/100)/12
#     valor_de_cuota=(r*monto*((1+r)**n)/(((1+r)**n)-1)
#     return valor_de_cuota
# años=int(input("Introduzca años del prestamo : "))
# interes_anual=float(input("Introduzca Tasa de Interes : "))
# Monto=int(input("Introduzca el Monto"))


# print("El valor de la cuota mensual es : {} " .format(valor_de_cuota(monto, interes_anual, años)))

# def valor_de_cuota(monto, interes, cuotas):

#     return monto * ((interes * ((1 + interes)**cuotas)) / (((1 + interes)**cuotas) - 1))

# monto = 1000000
# interes = (14.5/100)/12
# cuotas = 60

# print(valor_de_cuota(monto, interes, cuotas)
