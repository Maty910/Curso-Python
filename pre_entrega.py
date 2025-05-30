# Pre entrega 1 - Python
# Autor: Matías Chacón

# Declaración de la lista de productos
lista_productos = [
  ["Pitusas", "Galletitas", 1200]
]

# Menú de opciones para el usuario
while True: 
  print("" \
  "Menu de opciones: \n " \
  "1. Ingresar producto \n " \
  "2. Mostrar productos \n " \
  "3. Buscar producto \n " \
  "4. Modificar producto \n " \
  "5. Eliminar producto \n " \
  "6. Salir")

  opcion = int(input(f"Ingrese una opción: "))

  # Procesamiento de la opción seleccionada

  match opcion:
    case 1:
      # Ingreso de datos del producto
      while True:
        print("Opción 1 seleccionada: Ingresar producto")
        nombre_prod = str(input("Ingrese el nombre del producto: ").strip())
        if nombre_prod == "":
          print("El nombre del producto no puede estar vacío. Intente nuevamente.")
          continue
        if nombre_prod in lista_productos:
          print(f"El producto {nombre_prod} ya existe. Intente con otro nombre.")
          continue
        else:
          break

      print(f"El producto ingresado es: {nombre_prod}")

      # Validación del precio del producto
      while True:
        precio_prod = int(input("Ingrese el precio del producto:").strip())
        if precio_prod < 0:
          print("El precio debe ser mayor a cero. Intente nuevamete.")
          continue
        else:
          break
      print(f"El precio del producto {nombre_prod} ingresado es: ${precio_prod}")

      # Validación de la categoría del producto
      while True:
        categoria_prod = str(input("Ingrese la categoría del producto: ").strip())
        if categoria_prod == "":
          print("La categoría del producto no puede estar vacía. Intente nuevamente.")
          continue
        else:
          break
      print(f"La categoría del producto {nombre_prod} ingresada es: {categoria_prod}")

      # Agregar el producto a la lista de productos
      print(f"Producto {nombre_prod} añadido correctamente a la lista de productos.")

      producto = [nombre_prod, categoria_prod, precio_prod]
      lista_productos.append(producto)

    # Mostrar los productos ingresados
    case 2:
      print("Opción 2 seleccionada: Mostrar productos")
      if not lista_productos:
        print("No hay productos ingresados.")
        continue
      print("Productos ingresados:")
      for producto in lista_productos:
        nombre_prod, categoria_prod, precio_prod = producto
        print(f"\n Nombre: {nombre_prod} \n Precio: ${precio_prod} \n Categoría: {categoria_prod} \n")
        print(f"Detalles del último producto ingresado: {lista_productos[-1][0]}, ${lista_productos[-1][2]}, {lista_productos[-1][1]} \n \n")

    case 3:
      print("Opción 3 seleccionada: Buscar producto")
      buscar_prod = str(input("Ingrese el nombre del producto que desea buscar: ").strip())
      encontrado = False

      for producto in lista_productos:
        nombre_prod, categoria_prod, precio_prod = producto
        if buscar_prod.lower() in producto[0].lower():
          print(f" \n Producto encontrado: \n Nombre: {producto[0]} \n Precio: ${precio_prod} \n Categoría: {categoria_prod} \n")
          encontrado = True
          break
      if encontrado == False:
        print("Producto no encontrado, revise la información ingresada.")
    
    # Modificar producto existente
    case 4:
      print("Opción 4 ingresada: Modificar producto")
      modificar_prod = str(input("Ingrese el nombre del producto que desea modificar: "))
      encontrado = False
      for producto in lista_productos:
        nombre_prod, categoria_prod, precio_prod = producto
        if modificar_prod.lower() in producto[0].lower():
          print(f"Producto encontrado: {nombre_prod} \n Precio: ${precio_prod} \n Categoría: {categoria_prod} \n")
          encontrado = True
          break
        if encontrado == False:
          print("Producto no encontrado, revise la información ingresada.")  

      # Aquí se podría implementar la lógica para modificar el producto
      # # Por ejemplo, solicitar al usuario los nuevos datos del producto:
      print("Ingrese los nuevos datos del producto:")
      nombre_mod = str(input("Ingrese el nuevo nombre del producto: "))
      precio_mod = int(input("Ingrese el precio modificado del producto: ")) 
      categoria_mod = str(input("Ingrese la nueva categoría del producto: "))
      
      # Actualizar el producto en la lista
      for i, producto in enumerate(lista_productos): 
        if producto[0].lower() == modificar_prod.lower():
          lista_productos[i] = [nombre_mod, categoria_mod, precio_mod]
          print(f"Producto modificado: {nombre_mod} \n Precio: ${precio_mod} \n Categoría: {categoria_mod} \n")
          break
        
    # Eliminar producto existente
    case 5:
      print("Opción 5 ingresada: Seleccione que producto desea eliminar")
      nombre_prod = input("ingrese el nombre del producto que desea eliminar: ")
      if nombre_prod == nombre_prod:
        print(f"Producto eliminado: {nombre_prod}")
      else:
        print("Producto no encontrado, revise la información ingresada")
    case 6:
      print("Opción 6 seleccionada: Saliendo del programa")
      break
    case _:
      print("Opción no válidad. Por favor, ingrese una opción válida.")