import mysql.connector
from datetime import date

class ConexionBD:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="toor", 
            database="biblioteca"
        )
        self.cursor = self.conexion.cursor(dictionary=True)

    def ejecutar(self, sql, valores=None):
        self.cursor.execute(sql, valores or ())
        self.conexion.commit()

    def consultar(self, sql, valores=None):
        self.cursor.execute(sql, valores or ())
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()


class Libro:
    def __init__(self, titulo, autor, anio, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible


class Usuario:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo


class Prestamo:
    def __init__(self, id_usuario, id_libro):
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_prestamo = date.today()
        self.__fecha_devolucion = None

    def get_id_usuario(self):
        return self.__id_usuario

    def get_id_libro(self):
        return self.__id_libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion


def registrar_libro(db):
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    libro = Libro(titulo, autor, anio)
    db.ejecutar(
        "INSERT INTO libros (titulo, autor, anio, disponible) VALUES (%s, %s, %s, %s)",
        (libro.get_titulo(), libro.get_autor(), libro.get_anio(), libro.get_disponible())
    )
    print("✅ Libro registrado correctamente.\n")


def registrar_usuario(db):
    nombre = input("Nombre del usuario: ")
    tipo = input("Tipo (Alumno / Profesor / Otro): ")
    usuario = Usuario(nombre, tipo)
    db.ejecutar(
        "INSERT INTO usuarios (nombre, tipo) VALUES (%s, %s)",
        (usuario.get_nombre(), usuario.get_tipo())
    )
    print("✅ Usuario registrado correctamente.\n")


def registrar_prestamo(db):
    id_usuario = int(input("ID del usuario: "))
    id_libro = int(input("ID del libro: "))

    libro = db.consultar("SELECT * FROM libros WHERE id = %s", (id_libro,))
    if not libro:
        print("❌ Libro no encontrado.")
        return
    if not libro[0]["disponible"]:
        print("❌ Libro no disponible.")
        return

    prestamo = Prestamo(id_usuario, id_libro)
    db.ejecutar(
        "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)",
        (prestamo.get_id_usuario(), prestamo.get_id_libro(), prestamo.get_fecha_prestamo(), None)
    )
    db.ejecutar("UPDATE libros SET disponible = FALSE WHERE id = %s", (id_libro,))
    print("✅ Préstamo registrado correctamente.\n")


def devolver_libro(db):
    id_prestamo = int(input("ID del préstamo: "))
    prestamos = db.consultar("SELECT * FROM prestamos WHERE id = %s", (id_prestamo,))
    if not prestamos:
        print("❌ Préstamo no encontrado.")
        return

    id_libro = prestamos[0]["id_libro"]
    db.ejecutar("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s", (date.today(), id_prestamo))
    db.ejecutar("UPDATE libros SET disponible = TRUE WHERE id = %s", (id_libro,))
    print("✅ Libro devuelto correctamente.\n")


def listar_libros(db):
    libros = db.consultar("SELECT * FROM libros")
    print("\n📚 Lista de libros:")
    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} | {libro['titulo']} - {libro['autor']} ({libro['anio']}) - {estado}")
    print()


def listar_prestamos(db):
    prestamos = db.consultar("""
        SELECT p.id, u.nombre, l.titulo, p.fecha_prestamo, p.fecha_devolucion
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id
        JOIN libros l ON p.id_libro = l.id
    """)
    print("\n📖 Lista de préstamos:")
    for p in prestamos:
        devolucion = p["fecha_devolucion"] or "Pendiente"
        print(f"ID: {p['id']} | Usuario: {p['nombre']} | Libro: {p['titulo']} | Préstamo: {p['fecha_prestamo']} | Devolución: {devolucion}")
    print()


def menu():
    db = ConexionBD()
    while True:
        print("""
========= 📚 SISTEMA DE BIBLIOTECA =========
1. Registrar libro
2. Registrar usuario
3. Registrar préstamo
4. Devolver libro
5. Listar libros
6. Listar préstamos
0. Salir
""")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_libro(db)
        elif opcion == "2":
            registrar_usuario(db)
        elif opcion == "3":
            registrar_prestamo(db)
        elif opcion == "4":
            devolver_libro(db)
        elif opcion == "5":
            listar_libros(db)
        elif opcion == "6":
            listar_prestamos(db)
        elif opcion == "0":
            db.cerrar()
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.\n")


if __name__ == "__main__":
    menu()
