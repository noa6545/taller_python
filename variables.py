print("Ejercicio 1: Suma de dos números")
print (".."*20)
numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo número"))
print(f"Resultado: {numero1 + numero2}")


print (".."*20)
print("Ejercicio 2: Area de un rectangulo")
base = float(input("Ingrese la base del rectangulo:"))
altura = float(input("Ingrese la altura del rectangulo:"))
print(f"Resultado:{base * altura}")


print (".."*20)
print("Ejercicio 3: Minutos a horas y minutos")
minutos_totales = int(input("Ingrese la cantidad de minutos:"))
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")


print (".."*20)
print("Ejercicio 4: Precio con descuento")
precio = float(input("Ingrese el precio del producto:"))
descuento = float(input("Ingrese el porcentaje del descuento"))
valor_descuento = precio * (descuento/100)
precio_final = precio - valor_descuento
print(f"El precio final a pagar es: {precio_final}")


print (".."*20)
print("Ejercicio 5: Intercambio de variables")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
auxiliar = a
a = b
b = auxiliar 
print(f"Despues de intercambio: a = {a}, b = {b}")

 

print("Taller 1: Ejercicios para resolver")

print("Ejercicio 1: Solicitar el largo y ancho de un terreno rectangular y calcular su perimetro")
largo=float(input("Ingrese el largo del terrreno"))
ancho=float(input("Ingrese el ancho del terreno"))

print(f"El perimetro del terreno es:{2*largo+2*ancho}")

print("Ejercicio 2: Solicitar tres numeros y mostrar su promedio")
numero1 = (int(input("Ingresa el primer numero:")))
numero2 = (int(input("Ingresa el segundo numero")))
numero3 = (int(input("Ingresa el tercer numero")))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres numeros es: {promedio:.2f}")


print("Ejercicio 3: Solicitar el nombre y la edad de una persona y mostrar un mensaje de presentacion")
nombre = input("Ingrese su nombre por favor : ") #variable string (texto)
edad = int(input("Ingrese su edad por favor:")) #variable tipo entero
print(f"Hola! Mi nombre es: {nombre} y mi edad es: {edad}")


