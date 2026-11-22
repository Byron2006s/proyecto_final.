from abc import ABC, abstractmethod

# ==========================================================
# PROYECTO FINAL: ADOTATEK (Catálogo de Adopción)
# ==========================================================

# 1. ABSTRACCIÓN: Clase base abstracta que define la estructura
# general obligatoria y protege el estado mediante encapsulación.
class Mascota(ABC):

    def __init__(self, nombre, edad, raza, descripcion=""):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.descripcion = descripcion or "Sin descripción"
        self.__estado = "Disponible"  # ENCAPSULACIÓN: Atributo privado

    # Getter para consultar de forma segura el estado privado
    def obtener_estado(self):
        return self.__estado

    # Setter controlado para modificar el estado privado
    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado in ["Disponible", "Adoptado"]:
            self.__estado = nuevo_estado
        else:
            print("Estado no válido.")

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def mostrar_datos(self):
        pass


# 2. HERENCIA - Clase Perro (Hereda de Mascota)
class Perro(Mascota):

    def __init__(self, nombre, edad, raza, energia, descripcion=""):
        super().__init__(nombre, edad, raza, descripcion)
        self.energia = energia

    # 3. POLIMORFISMO: Comportamiento específico para el perro
    def hacer_sonido(self):
        return "Guau, guau"

    def mostrar_datos(self):
        return (
            f"[Perro] Nombre: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Raza: {self.raza} | "
            f"Energía: {self.energia} | "
            f"Estado: {self.obtener_estado()}\n"
            f"   Descripción: {self.descripcion}"
        )


# 2. HERENCIA - Clase Gato (Hereda de Mascota)
class Gato(Mascota):

    def __init__(self, nombre, edad, raza, independiente, descripcion=""):
        super().__init__(nombre, edad, raza, descripcion)
        self.independencia = "Sí" if independiente else "No"

    # 3. POLIMORFISMO: Comportamiento específico para el gato
    def hacer_sonido(self):
        return "Miau, miau"

    def mostrar_datos(self):
        return (
            f"[Gato] Nombre: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Raza: {self.raza} | "
            f"Independiente: {self.independencia} | "
            f"Estado: {self.obtener_estado()}\n"
            f"   Descripción: {self.descripcion}"
        )


# 2. HERENCIA - Clase para cualquier otro animal (Flexible)
class OtraMascota(Mascota):

    def __init__(self, tipo_animal, nombre, edad, raza, detalle,
                 descripcion="", sonido="Sonido característico"):
        super().__init__(nombre, edad, raza, descripcion)
        self.tipo_animal = tipo_animal.capitalize()
        self.detalle = detalle
        self.sonido = sonido

    # 3. POLIMORFISMO: Sonido personalizado según el animal ingresado
    def hacer_sonido(self):
        return self.sonido

    def mostrar_datos(self):
        return (
            f"[{self.tipo_animal}] Nombre: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Raza: {self.raza} | "
            f"Detalle: {self.detalle} | "
            f"Estado: {self.obtener_estado()}\n"
            f"   Descripción: {self.descripcion}"
        )


# ==========================================================
# GESTOR DEL CATÁLOGO Y OPERACIONES
# ==========================================================
class CentroAdopciones:

    def __init__(self):
        self.registro = []   # Lista general de mascotas
        self.favoritos = []  # Lista personal de favoritos

    # Método para registrar una nueva mascota en el sistema
    def registrar(self, mascota):
        self.registro.append(mascota)

    # Método para mostrar todo el catálogo enumerado
    def mostrar_catalogo(self):
        print("\n================ CATÁLOGO DE MASCOTAS ================")

        if not self.registro:
            print("No hay mascotas registradas.")
            return

        for i, m in enumerate(self.registro, 1):
            print(f"{i}. {m.mostrar_datos()}")
            print(f"   Sonido: {m.hacer_sonido()}")

        print("======================================================")

    # Método para buscar mascotas por nombre de forma parcial/total
    def buscar(self, nombre):
        if not nombre.strip():
            print("Debes ingresar un nombre para buscar.")
            return

        print("\n================ RESULTADO DE BÚSQUEDA ================")

        encontrados = [
            m for m in self.registro
            if nombre.lower() in m.nombre.lower()
        ]

        if not encontrados:
            print("No se encontró ninguna coincidencia.")
        else:
            for m in encontrados:
                print(m.mostrar_datos())

        print("======================================================")

    # Método para filtrar por tipo de animal y/o disponibilidad
    def filtrar(self, tipo="", solo_disponibles=False):
        print("\n================ RESULTADO DEL FILTRO ================")

        encontrados = []
        for m in self.registro:
            nombre_tipo = type(m).__name__
            if isinstance(m, OtraMascota):
                nombre_tipo = m.tipo_animal

            if tipo and tipo.lower() not in nombre_tipo.lower():
                continue
            if solo_disponibles and m.obtener_estado() != "Disponible":
                continue
            encontrados.append(m)

        if not encontrados:
            print("No hay mascotas que coincidan con el filtro.")
        else:
            for m in encontrados:
                print(m.mostrar_datos())

        print("======================================================")

    # Método para agregar mascotas a la lista de favoritos con validaciones
    def agregar_favorito(self, idx):
        if 0 <= idx < len(self.registro):
            m = self.registro[idx]

            if m.obtener_estado() == "Adoptado":
                print(
                    f"{m.nombre} ya fue adoptado y no se puede "
                    "agregar a favoritos."
                )
            elif m in self.favoritos:
                print("Esta mascota ya está en tus favoritos.")
            else:
                self.favoritos.append(m)
                print(f"¡Éxito! {m.nombre} fue añadido a tus favoritos.")
        else:
            print("Error: Número de mascota inválido.")

    # Método para eliminar mascotas de la lista de favoritos
    def quitar_favorito(self, idx):
        if 0 <= idx < len(self.favoritos):
            m = self.favoritos.pop(idx)
            print(f"{m.nombre} fue eliminado de tus favoritos.")
        else:
            print("Error: Número de favorito inválido.")

    # Método para ver la lista de favoritos actual
    def ver_favoritos(self):
        print("\n================== MIS FAVORITOS ==================")

        if not self.favoritos:
            print("No tienes favoritos guardados.")
            print("===================================================")
            return

        for i, m in enumerate(self.favoritos, 1):
            print(
                f"{i}. {m.nombre} ({m.raza}) | "
                f"Estado: {m.obtener_estado()}"
            )

        print("===================================================")

    # Método para procesar la adopción cambiando el estado encapsulado
    def adoptar(self, idx):
        if 0 <= idx < len(self.registro):
            m = self.registro[idx]

            if m.obtener_estado() == "Disponible":
                m.actualizar_estado("Adoptado")
                print(
                    f"¡Felicidades! {m.nombre} "
                    "ha sido adoptado con éxito."
                )
            else:
                print(f"Lo sentimos, {m.nombre} ya fue adoptado.")
        else:
            print("Error: Número de mascota inválido.")


# ==========================================================
# PROGRAMA PRINCIPAL Y MENÚ INTERACTIVO
# ==========================================================
if __name__ == "__main__":

    centro = CentroAdopciones()

    # Precarga inicial de mascotas para el catálogo
    centro.registrar(
        Perro("Solovino", 2, "Pastor Alemán", "Alto",
              "Leal y juguetón, ideal para familias activas")
    )
    centro.registrar(
        Gato("Luna", 1, "Siamés", True,
             "Tranquila y cariñosa, vacunada y esterilizada")
    )
    centro.registrar(
        OtraMascota("Loro", "Oro", 2, "Ave", "Hablador",
                    "Aprende palabras rápido y le gusta la compañía",
                    "Cra, cra")
    )

    # Bucle principal del menú interactivo
    while True:

        print("\n========== MENÚ ADOTATEK ==========")
        print("1. Ver catálogo de mascotas")
        print("2. Buscar mascota por nombre")
        print("3. Filtrar por tipo o disponibilidad")
        print("4. Registrar nueva mascota")
        print("5. Agregar a favoritos")
        print("6. Quitar de favoritos")
        print("7. Ver mis favoritos")
        print("8. Adoptar mascota")
        print("9. Salir")
        print("==================================")

        op = input("Elige una opción (1-9): ").strip()

        if op == "1":
            centro.mostrar_catalogo()

        elif op == "2":
            nombre_buscado = input(
                "Escribe el nombre a buscar: "
            ).strip()
            centro.buscar(nombre_buscado)

        elif op == "3":
            tipo_filtro = input(
                "Tipo de animal (Enter para todos): "
            ).strip()
            disp = input(
                "¿Solo disponibles? (s/n): "
            ).strip().lower()

            if disp not in ["s", "n"]:
                print("Respuesta incorrecta. Escribe s o n.")
                continue

            centro.filtrar(tipo_filtro, disp == "s")

        elif op == "4":
            print("\n--- REGISTRO DE NUEVA MASCOTA ---")
            tipo = input(
                "¿Qué animal deseas registrar? "
                "(Ej: Perro, Gato, Conejo, Loro): "
            ).strip().lower()

            if not tipo:
                print("Debes ingresar el tipo de animal.")
                continue

            nombre = input("Nombre: ").strip()
            if not nombre:
                print("El nombre es obligatorio.")
                continue

            try:
                edad = int(input("Edad: "))
            except ValueError:
                print("Error: La edad debe ser un número entero.")
                continue

            if edad < 0:
                print("La edad no puede ser negativa.")
                continue

            raza = input("Raza o tipo: ").strip()
            if not raza:
                print("La raza es obligatoria.")
                continue

            descripcion = input(
                "Descripción del perfil (Enter para omitir): "
            ).strip()

            # Enrutamiento según el tipo de mascota ingresado
            if "perro" in tipo:
                energia = input("Nivel de energía: ").strip()
                if not energia:
                    print("Debes ingresar el nivel de energía.")
                    continue
                centro.registrar(
                    Perro(nombre, edad, raza, energia, descripcion)
                )

            elif "gato" in tipo:
                ind_input = input(
                    "¿Es independiente? (s/n): "
                ).strip().lower()
                if ind_input not in ["s", "n"]:
                    print("Respuesta incorrecta. Escribe s o n.")
                    continue
                centro.registrar(
                    Gato(nombre, edad, raza, ind_input == "s", descripcion)
                )

            else:
                detalle = input(
                    "Detalle o característica especial: "
                ).strip()
                if not detalle:
                    print("Debes ingresar una característica.")
                    continue

                sonido = input(
                    "Sonido que hace (Enter para omitir): "
                ).strip() or "Sonido característico"

                centro.registrar(
                    OtraMascota(
                        tipo, nombre, edad, raza, detalle,
                        descripcion, sonido
                    )
                )

            print(f"¡{nombre} se ha registrado exitosamente!")

        elif op == "5":
            centro.mostrar_catalogo()
            try:
                idx = int(input(
                    "Ingresa el número de la mascota para favoritos: "
                )) - 1
                centro.agregar_favorito(idx)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif op == "6":
            centro.ver_favoritos()
            if centro.favoritos:
                try:
                    idx = int(input(
                        "Ingresa el número del favorito a quitar: "
                    )) - 1
                    centro.quitar_favorito(idx)
                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif op == "7":
            centro.ver_favoritos()

        elif op == "8":
            centro.mostrar_catalogo()
            try:
                idx = int(input(
                    "Ingresa el número de la mascota que deseas adoptar: "
                )) - 1
                centro.adoptar(idx)
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif op == "9":
            print("Saliendo del sistema AdotaTek. ¡Hasta pronto!")
            break

        else:
            print("Opción incorrecta. Inténtalo de nuevo.")