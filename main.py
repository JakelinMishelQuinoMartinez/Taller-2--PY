from inventario import productos
def menu_principal():
    print("=" * 40)
    print("Menú Principal")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
    print("=" * 40)

def agregar_producto():
    print("=" * 40)
    print("AÑADIR NUEVO PRODUCTO")
    print("=" * 40)
    nombre = input("Nombre del producto: ").lower()
    nombres_existentes = [p['nombre'].lower() for p in productos]
    if nombre.lower() in nombres_existentes:
        print(f"Aviso: El producto '{nombre}' ya existe.")
        return
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad disponible: "))
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(nuevo_producto)
        print(f"\nEl producto '{nombre}' ha sido agregado al inventario.")
        print("Volviendo al inicio...\n")
    except ValueError:
        print("\nError: El precio y la cantidad deben ser valores numéricos.")

def listar_productos():
    pass

def actualizar_cantidad():
    pass

def eliminar_producto():
    pass

def calcular_valor():
    pass

while True:
    menu_principal()
    try:
        opc = int(input("Ingrese su opción: "))
        if opc == 1:
            agregar_producto()
        elif opc == 2:
            listar_productos()
        elif opc == 3:
            actualizar_cantidad()
        elif opc == 4:
            eliminar_producto()
        elif opc == 5:
            calcular_valor()
        elif opc == 6:
            print("Saliendo...")
            break
        else:
            print("Error: El número debe estar entre 1 y 6.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")