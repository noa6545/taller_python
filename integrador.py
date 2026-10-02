while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes >0:
            break
        else:
            print("La cantidad debe ser mayor a Cero")
        
    except ValueError:
        print("Debe ingresar un numero entero")
        
suma_promedio = 0
aprobados = 0
reprobados = 0

for estudiante in range (1, cantidad_estudiantes + 1):
    print("Estudiante", estudiante)
    nombre = input("Nombre: ")
    
    while True:
        try:
            nota1 = float(input("Primera nota (0-5): "))
            if nota1 >=0 and nota1 <=5:
                break
            else:
                print("La nota debe ser entre 0 y 5")
        except ValueError:
            print("Debe ingresar un numero valido")
            
    while True:
        try:
            nota2 = float(input("Segunda nota (0-5): "))
            if nota2 >=0 and nota2 <=5:
                break
            else:
                print("La nota debe ser entre 0 y 5")
        except ValueError:
            print("Debe ingresar un numero valido")
            
    while True:
        try:
            nota3 = float(input("Tercera nota (0-5): "))
            if nota3 >=0 and nota3 <=5:
                break
            else:
                print("La nota debe ser entre 0 y 5")
        except ValueError:
            print("Debe ingresar un numero valido")
            
    promedio = (nota1 + nota2 + nota3)/3
    if promedio >=3:
        print("Promedio", round(promedio,2))
        print("Estado: Aprobado")
        aprobados=aprobados+1
    else:
        print("Promedio", round(promedio,2))
        print("Estado: Reprobado")
        reprobados=reprobados+1
        
    suma_promedio = suma_promedio + promedio 
    
#Calcular promedio general
promedio_grupo =suma_promedio/cantidad_estudiantes

#Mostrar resumen 
print("\n========================")
print("    RESUMEN DEL GRUPO ")
print("========================")
print("Total estudiantes: ", cantidad_estudiantes)
print("Aprobados: ", aprobados)
print("Reprobados: ", reprobados)
print("Promedio general: ", round(promedio_grupo, 2))
print("========================")

    