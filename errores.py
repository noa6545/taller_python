"""while True:
    try:
        nota = float(input("Ingrese su nota: "))
    except ValueError:
        print("Ingresa una nota válida.")"""
        
"""while True:
    try:
        cantidad_notas = int(input("Cuantas notas quieres registrar: "))
        
        #Crear For - para solicitar las notas.
        lista_notas = []
        for i in range (cantidad_notas):
            try:
                nota = float(input("Ingrese nota: "))
                lista_notas.append(nota)
            except ValueError:
                print ("Nota Invalida")
        print("Notas Registradas: ", lista_notas)
        promedio =sum(lista_notas)/len(lista_notas)
        print(f"Promedio: {promedio}")
        
        if promedio <=2:
            print("Muy mal")
        elif promedio <=3:
            print("Basico")
        elif promedio <=4:
            print("Aceptable")
        elif promedio <=5:
            print("Bien")
        else:
            print("Nota invalida")
        
    except ValueError:
        print ("Ingrese una cantidad valida") """
        
        
"""      
#Ejercicio 1: try/except basico
#Sin manejo de errores, ingresar "hola" en lugar de un numero
#Provocaria un ValueError y el programa se detendria
try:
    numero = int(input("Ingrese un numero entero: "))
    print(f"El numero ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un numero entero valido.")
    
#Ejercicio 2: Division segura con ZeroDivisionError
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividendo /divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado} ")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese unicamente valores numericos.")
    
#Ejercicio 3: else y finally
#else - se ejecuta solo si NO ocurrio ninguna excepcion
#finally - se ejecuta SIEMPRE, con o sin error
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un numero entero ")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada")
    
#Ejercicio 4: Solicitar un dato valido hasta que el usuario lo ingrese correctamente
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        break    #sale del ciclo si el valor es valido
    except ValueError as e:
        print(f"Entrada invalida: {e}. Intente de nuevo")
print(f"Nota registrada: {nota}")      

## Ejercicio 5: raise — lanzar una excepción personalizada
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}") """
    
#TALLER
#Punto 1: Solicitar número y operador
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    operador = input("Ingresa el operador (+, -, *, /): ")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        print("Operador no válido.")
        resultado = None

    if resultado is not None:
        print("Resultado:", resultado)

except ValueError:
    print("Error: debes ingresar números válidos.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.") 

    
#Punto 2: Nombre de archivo
nombre_archivo = input("Ingresa el nombre del archivo: ")

try:
    archivo = open(nombre_archivo, "r")

    contenido = archivo.read()

    print("Contenido del archivo:")
    print(contenido)

    archivo.close()

except FileNotFoundError:
    print("Error: el archivo no fue encontrado.")


#Punto 3: Formato de fecha DD/MM/AAAA
from datetime import datetime

fecha = input("Ingresa una fecha (DD/MM/AAAA): ")

try:
    fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")

    print("La fecha es válida.")
    print("Fecha:", fecha_valida.strftime("%d/%m/%Y"))

except ValueError:
    print("Error: la fecha no es válida.")
    print("Debes utilizar el formato DD/MM/AAAA.")
    
#Punto 4: Raiz cuadrada
import math

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo.")

    return math.sqrt(n)


try:
    numero = float(input("Ingresa un número: "))

    resultado = raiz_cuadrada(numero)

    print("La raíz cuadrada es:", resultado)

except ValueError as error:
    print("Error:", error)

    
#Punto 5: Ingreso de numeros
suma = 0
cantidad = 0

while True:
    entrada = input("Ingresa un número o escribe 'fin' para terminar: ")

    if entrada.lower() == "fin":
        break

    try:
        numero = float(entrada)

        suma += numero
        cantidad += 1

    except ValueError:
        print("Entrada inválida. Ese valor será ignorado.")


if cantidad > 0:
    promedio = suma / cantidad

    print("\nResultados:")
    print("Cantidad de valores aceptados:", cantidad)
    print("Promedio:", promedio)

else:
    print("\nNo se ingresaron valores válidos.")
    
