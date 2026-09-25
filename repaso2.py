#Ciclos
"""lista_producto = [] #Lista en blanco
cantidad = int(input("Cantidad de productos a comprar: "))

for i in range(cantidad):
    producto= input(f"Nombre del producto {i+1}: ")
    #Agregar producto a la lista
    lista_producto.append(producto)
print (f"Productos comprados: {lista_producto}")"""

lista_perros = []
lista_gatos = []
while True:
    pregunta = int(input("""
    1. Registrar Perritos 🐕‍🦺
    2. Registrar Gatitos 🐈‍⬛
    3. Listado Perritos 🐾
    4. Listado Gatitos 🐈
    5. Salir
    """))
    
    if pregunta ==1:
        perro= input("Ingrese nombre del perro: ")
        lista_perros.append(perro)
        print ("Perrito Registrado")
    elif pregunta ==2:
        gato= input("Ingrese nombre del gato: ")
        lista_gatos.append(gato)
        print ("Gatito Registrado")
    elif pregunta ==3:
        print("Listado de perritos", lista_perros)
    elif pregunta ==4:
        print("Listado de gatitos", lista_gatos )
    elif pregunta ==5:
        print("Saliendo del sistema")
        break
    else:
        print("Opción Inválida")
        break        