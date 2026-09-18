"""
Condicionales: que permite validar cuando se cumple o no con una condicion

#crear variables
print("Por favor ingrese los siguientes datos/n")
var_nombre = input("Por favor ingresa tu nombre: ")
var_edad = int(input("Por favor ingrese su edad: "))

#crear condicion
if var_edad >= 18 :
    print (f"{var_nombre} Eres mayor de edad.")
else: 
    print (f"{var_nombre} Eres menor de edad.")
    
  #crear variable
print("Ejercicio: nota final")
var_nombre = input("Nombre: ")
var_notafinal = float(input("Nota final: "))

if var_notafinal < 0 or var_notafinal >5:
    print("Nota invalida.")
elif var_notafinal >= 3.5 :
    print(f"Estudiante {var_nombre} GANOO 💕🎊")
else: 
    print(f"Estudiante {var_nombre} PERDIO 😞🚫")
    
    

    
    #Ejercicio 1: Determinar si es positivo o negativo 
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")
    
    
#Ejercicio 2: Verificar si una pesona es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
        

#Ejercicio 3: Determinar si el numero es par o impar
numero = int(input("Ingrese un numero entero:"))
if numero % 2 == 0: 
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
    
    
#Ejercicio 4: Clasificar una nota academica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))
if nota > 4.5:
    print("Desempeño Superior")
elif nota > 3.5:
    print("Desempeño Alto")
elif nota > 3.0:
    print("Desempeño Basico")
else:
    print("Desempeño Bajo")    

    
#Ejercicio 5: Determinar el mayor de los tres numeros
n1 = float(input("Ingrese el primer numero: "))  
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))
if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
else: 
    mayor = n3
    print(f"El mayor de los tres numeros es: {mayor} ")
    
    #taller
    #punto1
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Error, edad invalida")
elif edad <18:
    print(f"Faltan {18-edad} años para ser mayor")
else: 
    print ("Eres mayor de edad") 
    
    #punto2
nombre = input("Ingresa tu nombre: ")
nota_final = float(input("Ingresa tu nota en una escala de 0.0 a 5.0: "))
if nota_final < 0.0 or nota_final > 5 :
    print("Error, nota invalida ")
elif nota_final <3.0:
    print(f"{nota_final} Insuficiente")
elif nota_final <3.4:
    print(f"{nota_final} Aceptable")
elif nota_final <4.4:
    print(f"{nota_final} Bueno")
else:
    print(f"{nota_final} Excelente") 
    """
    
    #punto3
nombre = input("Nombre: ")   
total_compra = float(input("Total compra: "))
    
if total_compra < 100000:
    print(f"""
          - Cliente: {nombre}
          - Compra: {total_compra} No tiene descuento
          """)
elif total_compra < 299999:    
    #Descuento 10%
    print(f"""
          - Cliente: {nombre}
          -Compra: {total_compra}
          - Descuento: {total_compra * 0.1}
          - Total pagar: {total_compra - (total_compra*0.1)}
          """)
elif total_compra < 499999:    
    #Descuento 15%
    print(f"""
          - Cliente: {nombre}
          -Compra: {total_compra}
          - Descuento: {total_compra * 0.15}
          - Total pagar: {total_compra - (total_compra*0.15)}
          """)
else:
    print(f"""
          - Cliente: {nombre}
          -Compra: {total_compra}
          - Descuento: {total_compra * 0.2}
          - Total pagar: {total_compra - (total_compra*0.2)}
          """)
    
    
nombre_ciudad = input("Nombre de la ciudad: ")
temperatura_ciudad = int(input("Temperatura de la ciudad:"))   
if temperatura_ciudad <=10:
    print(f"La ciudad de {nombre_ciudad} tiene una temperatura de {temperatura_ciudad} grados, le podria dar hipotermia... Recomendacion: No salir de casa. ")
elif temperatura_ciudad in range (10, 18):
    print(f"La ciudad de {nombre_ciudad} tiene una temperatura de {temperatura_ciudad} grados, esta haciendo frio... Recomendacion: Si va a salir pongase chaqueta")
elif temperatura_ciudad in range (18 , 25):
    print(f"La ciudad de {nombre_ciudad} tiene una temperatura de {temperatura_ciudad} grados, esta a temperatura ambiente... Recomendacion: Si va a salir lleve un abanico")
elif temperatura_ciudad in range (26 , 32):
    print(f"La ciudad de {nombre_ciudad} tiene una temperatura de {temperatura_ciudad} grados, esta haciendo demasiado calor... Recomendacion: Tome una ducha y lleve sombrilla si va a salir")

    
    
          

