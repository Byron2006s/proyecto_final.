class Producto:
    """
    Representa un producto o servicio dentro del sistema de inventario.
    Utiliza principios de Programación Orientada a Objetos (POO) como encapsulamiento
    y propiedades con validación.
    """
    def __init__(self, codigo, nombre, precio, existencias, categoria):
        # Atributos privados para proteger los datos (encapsulamiento)
        self._codigo = codigo
        self._nombre = nombre
        self._precio = float(precio)
        self._existencias = int(existencias)
        self._categoria = categoria

    # Getters y Setters con validación usando decoradores @property
    @property
    def codigo(self):
        """Devuelve el código del producto."""
        return self._codigo

    @property
    def nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    @property
    def precio(self):
        """Devuelve el precio actual del producto."""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        """Valida que el nuevo precio no sea negativo antes de asignarlo."""
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(nuevo_precio)

    @property
    def existencias(self):
        """Devuelve la cantidad de existencias disponibles."""
        return self._existencias

    @existencias.setter
    def existencias(self, nuevas_existencias):
        """Valida que las nuevas existencias no sean negativas antes de asignarlas."""
        if nuevas_existencias < 0:
            raise ValueError("Las existencias no pueden ser negativas.")
        self._existencias = int(nuevas_existencias)

    @property
    def categoria(self):
        """Devuelve la categoría a la que pertenece el producto."""
        return self._categoria

    def mostrar_informacion(self):
        """Retorna una cadena con los detalles formateados del producto."""
        return f"Código: {self._codigo} | Nombre: {self._nombre} | Precio: Q {self._precio:.2f} | Existencias: {self._existencias} | Categoría: {self._categoria}"


class Inventario:
    """
    Gestiona una colección (lista) de objetos de la clase Producto,
    permitiendo agregarlos, buscarlos, actualizarlos, eliminarlos y realizar cálculos.
    """
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos del inventario
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto nuevo al inventario tras validar que su código no esté duplicado."""
        for p in self.productos:
            if p.codigo == producto.codigo:
                raise ValueError("Ya existe un producto con ese código.")
        self.productos.append(producto)

    def buscar_por_codigo(self, codigo):
        """Busca y retorna un producto según su código único. Retorna None si no existe."""
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def mostrar_inventario(self):
        """Muestra en consola la lista completa de todos los productos registrados."""
        print("\n" + "="*50)
        print("        INVENTARIO COMPLETO DE LA TIENDA")
        print("="*50)
        if not self.productos:
            print("El inventario está actualmente vacío.")
        else:
            for i, p in enumerate(self.productos, 1):
                print(f"{i}. {p.mostrar_informacion()}")
        print("="*50)

    def calcular_valor_total(self):
        """Calcula el valor económico total de todo el inventario (precio por existencias)."""
        total = sum(p.precio * p.existencias for p in self.productos)
        return total

    def mostrar_existencias_bajas(self, limite=5):
        """Filtra y muestra los productos cuyas existencias sean menores al límite establecido (por defecto 5)."""
        print(f"\n--- PRODUCTOS CON EXISTENCIAS BAJAS (Menor a {limite}) ---")
        encontrados = False
        for p in self.productos:
            if p.existencias < limite:
                print(p.mostrar_informacion())
                encontrados = True
        if not encontrados:
            print("No hay productos con existencias bajas.")

    def eliminar_producto(self, codigo):
        """Elimina un producto del inventario basándose en su código. Retorna True si se eliminó, False si no."""
        p = self.buscar_por_codigo(codigo)
        if p:
            self.productos.remove(p)
            return True
        return False


def menu():
    """
    Controla la interfaz de usuario por consola, gestionando el menú interactivo,
    la captura de opciones, los datos precargados y el manejo de excepciones.
    """
    inv = Inventario()
    
    # Datos precargados iniciales de la tienda y soporte técnico
    try:
        inv.agregar_producto(Producto("101112", "Laptop HP Victus i5 13a Gen", 6500.00, 3, "Laptops"))
        inv.agregar_producto(Producto("101113", "CPU Ensamblado Core i7 / 16GB RAM", 5200.00, 2, "Computadoras de Escritorio"))
        inv.agregar_producto(Producto("101114", "Mouse Gamer RGB USB", 150.00, 15, "Accesorios"))
        inv.agregar_producto(Producto("101115", "Teclado Mecánico Español", 350.00, 4, "Accesorios"))
        inv.agregar_producto(Producto("101116", "Mantenimiento Preventivo (Limpieza y Pasta Térmica)", 250.00, 99, "Servicios"))
    except Exception:
        pass

    # Bucle principal del menú interactivo
    while True:
        print("\n=============================================")
        print("   SISTEMA DE TIENDA Y MANTENIMIENTO TÉCNICO")
        print("=============================================")
        print("1. Agregar producto o servicio")
        print("2. Mostrar inventario completo")
        print("3. Buscar por código")
        print("4. Actualizar existencias")
        print("5. Actualizar precio")
        print("6. Mostrar productos con existencias bajas")
        print("7. Mostrar valor total del inventario")
        print("8. Eliminar producto o servicio")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            # Opción 1: Registrar un nuevo ítem
            if opcion == 1:
                codigo = input("Ingrese el código numérico (ej. 101117): ").strip()
                nombre = input("Ingrese el nombre del artículo/servicio: ").strip()
                precio = float(input("Ingrese el precio (Q): "))
                existencias = int(input("Ingrese la cantidad disponible/existencias: "))
                print("Sugerencias de Categoría: Laptops, Computadoras de Escritorio, Accesorios, Servicios")
                categoria = input("Ingrese la categoría: ").strip()
                
                nuevo_prod = Producto(codigo, nombre, precio, existencias, categoria)
                inv.agregar_producto(nuevo_prod)
                print("¡Item ingresado exitosamente!")
                
            # Opción 2: Ver todos los productos
            elif opcion == 2:
                inv.mostrar_inventario()
                
            # Opción 3: Buscar un producto por código
            elif opcion == 3:
                codigo = input("Ingrese el código a buscar: ").strip()
                p = inv.buscar_por_codigo(codigo)
                if p:
                    print("\n--- ITEM ENCONTRADO ---")
                    print(p.mostrar_informacion())
                else:
                    print("No se encontró ningún artículo o servicio con ese código.")
                    
            # Opción 4: Actualizar stock/existencias
            elif opcion == 4:
                codigo = input("Ingrese el código del producto/servicio: ").strip()
                p = inv.buscar_por_codigo(codigo)
                if p:
                    nuevas_ex = int(input(f"Existencias actuales ({p.existencias}). Ingrese nuevas existencias: "))
                    p.existencias = nuevas_ex
                    print("¡Existencias actualizadas con éxito!")
                else:
                    print("Item no encontrado.")
                    
            # Opción 5: Actualizar precio
            elif opcion == 5:
                codigo = input("Ingrese el código del producto/servicio: ").strip()
                p = inv.buscar_por_codigo(codigo)
                if p:
                    nuevo_pr = float(input(f"Precio actual (Q {p.precio:.2f}). Ingrese nuevo precio: "))
                    p.precio = nuevo_pr
                    print("¡Precio actualizado con éxito!")
                else:
                    print("Item no encontrado.")
                    
            # Opción 6: Ver alertas de bajo stock
            elif opcion == 6:
                inv.mostrar_existencias_bajas()
                
            # Opción 7: Calcular el valor monetario total del inventario
            elif opcion == 7:
                total = inv.calcular_valor_total()
                print(f"\nValor total del inventario disponible: Q {total:.2f}")
                
            # Opción 8: Eliminar un ítem
            elif opcion == 8:
                codigo = input("Ingrese el código del ítem a eliminar: ").strip()
                if inv.eliminar_producto(codigo):
                    print("¡Item eliminado correctamente!")
                else:
                    print("No se encontró el código especificado.")
                    
            # Opción 0: Salir del sistema
            elif opcion == 0:
                print("¡Saliendo del sistema! Gracias.")
                break
            else:
                print("Opción inválida. Por favor, elija un número del menú.")
                
        # Manejo de errores en las entradas del usuario o reglas de negocio
        except ValueError as e:
            print(f"Error de validación o entrada incorrecta: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada principal del script en Python
if __name__ == "__main__":
    menu()