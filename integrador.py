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
aprobado = 0
reprobado = 0

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
            

    