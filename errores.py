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
    print(f"Error: {e}")