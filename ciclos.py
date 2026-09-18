"""
for i in range(2, 11, 2):
    print(f"{i} - Vampire diaries ")

mensaje = input("Escribe tu mesaje: ")
repeticion = int(input("Cuantas veces quieres repetir el mensaje: "))
for i in range(repeticion):
    print(f"{i + 1} - {mensaje}") """
    
#Preguntar nombre estudiante
#Preguntar al profe cuantas notas quiere registrar.
#Hacer el promedio de las notas y mostrarlo
#Promedio >=3.5   Mostar Estudiante gano - contrario perdio
"""
print("=== Sistema de calificacion. ===") 
estudiante = input("Nombre del estudiante: ")
can_notas = int(input("Cuantas veces vas a registrar: "))

promedio = 0
for i in range(can_notas):
    notas=float(input(f"Ingrese nota {i+1} : "))
    
    if notas not in range (0, 5):
        print("Nota Invalida")
        break
    
    promedio += notas
    
promedio_final =promedio/can_notas 
if (promedio_final) >=3.5:
    print(f" El estudiante {estudiante} - promedio {promedio_final:.1f} Gano 🎊")
else:
    print(f" El estudiante {estudiante} - promedio {promedio_final:.1f} Perdio 🚫")
"""

while True:
    menu = int(input("""
               Seleccione Opcion a realizar :
               1. Sumar
               2. Restar
               3. Salir
               :    """))
    
    if menu == 1:
        n1 = int(input ("Ingrese n1: "))
        n2 = int(input ("Ingrese n2: "))
        print(f"Resultado {n1 + n2} ")
    elif menu == 2:
        n1 = int(input ("Ingrese n1: "))
        n2 = int(input ("Ingrese n2: "))
        print(f"Resultado {n1 - n2} ")
    elif menu == 3:
        print("Saliendo del sistema")
        break 
    else:
        print("Opcion Invalida")








