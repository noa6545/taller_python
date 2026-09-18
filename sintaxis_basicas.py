#creacion de variables
nombre = "Noa" #variable string (texto)
documento = 123 #variable tipo entero
direccion = "Medellin crr 46"

tiene_deuda = True
#Mostrar informacion en pantalla.
print(nombre)
print("CONCATENACION USANDO +")
print("=" * 30)

print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)
print("Mi nombre es:", nombre, "y mi documento es:", documento, "Mi direccion es: ", direccion, "Tienes Deuda?:", tiene_deuda)

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)
print(f"Nombre : {nombre} Documento: {documento} Direccion {direccion}")

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)
print(f"""
      -Nombre: {nombre}
      -Documento: {documento}
      -Direccion: {direccion}
      -Tienes deudas?: {tiene_deuda}
     """)

print(f"\n Hola, {nombre}")
print(f"Bienvenida {nombre} a Python.\n")