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
    pass

def listar_productos():
    pass

def actualizar_cantidad():
    print("=" * 40)
    print("ACTUALIZAR CANTIDAD DE UN PRODUCTO")
    print("=" * 40)
    nombre_buscar = input("Ingrese el nombre del producto a modificar: ").lower()
    encontrado = False
    for p in productos:
        if p['nombre'].lower() == nombre_buscar:
            encontrado = True
            print(f"\nProducto encontrado: {p['nombre']}")
            print(f"Cantidad actual: {p['cantidad']}")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                p['cantidad'] = nueva_cantidad
                print(f"La cantidad de '{p['nombre']}' ha sido actualizada.")
            except ValueError:
                print("Error: Debe ingresar un número entero para la cantidad.")
            break 
    if not encontrado:
        print(f"\nError: El producto '{nombre_buscar}' no existe en el inventario.")

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