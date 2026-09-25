#Variables
print("=== Tienda Donde Noa ===")

print("Por favor ingrese la siguiente información: \n")
cliente =input("Nombre del cliente: ")
producto =input("Nombre del producto: ")
cantidad =int(input("Cantidad: "))
precio =float(input("Precio: "))

#Variable para preguntar si la compra es a domicilio
domicilio =input("La compra es para domicilio (SI - NO): ")
#Condicional verificar que respondio el usuario

#.upper() convierte en mayuscula  .lower() minuscula
if domicilio.upper() == "NO":
    print("=== RESUMEN COMPRA ===")
    print(f"""
    -Cliente : {cliente}
    -Producto : {producto}
    -Cantidad : {cantidad}
    -Precio : {precio}
    -Total : {cantidad*precio}
      
      GRACIAS POR SU COMPRA 🛒💕 """)
    
elif domicilio.upper() == "SI":
    direccion = input("Ingrese Municipio de envio (Medellín, Itaguí, Bello): ")
    
    valor_domicilio = 0
    if direccion.lower() == "medellin":
        valor_domicilio = 5000
    elif direccion.lower() == "itagui":
        valor_domicilio = 10000
    elif direccion.lower() == "bello":
        valor_domicilio = 8000
    else:
        print("Dirección Inválida")
        
    #Mostrar resumen venta
    print("=== RESUMEN COMPRA ===")
    print(f"""
    -Cliente : {cliente}
    -Producto : {producto}
    -Cantidad : {cantidad}
    -Precio : {precio}
    -Subtotal : {cantidad*precio}
    -Domicilio : {valor_domicilio}
    -Total pagar : {valor_domicilio + (cantidad*precio)}

    GRACIAS POR SU COMPRA 🛒💕 """)
    
else: 
    print("Opción Inválida")
            