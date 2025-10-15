<img width="1920" height="1080" alt="Captura de pantalla (13)" src="https://github.com/user-attachments/assets/df45d3fc-73e8-4193-8b9b-cd346f17022d" />

📚 Sistema de Biblioteca en Python + MySQL
🧾 Descripción del proyecto

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python con conexión a una base de datos MySQL.
Permite registrar libros, usuarios, préstamos y devoluciones, así como consultar el estado de los libros y el historial de préstamos.
Su objetivo es simular el funcionamiento básico de una biblioteca, aplicando conceptos de POO (Programación Orientada a Objetos) y bases de datos relacionales.

⚙️ Funcionalidades principales
🔹 1. Registrar libro

Permite agregar nuevos libros a la base de datos con su título, autor, año y disponibilidad.

🔹 2. Registrar usuario

Permite registrar usuarios de tipo Alumno, Profesor u Otro.

🔹 3. Registrar préstamo

Asocia un libro disponible con un usuario y guarda la fecha del préstamo.
Automáticamente cambia el estado del libro a no disponible.

🔹 4. Devolver libro

Permite marcar un préstamo como devuelto y vuelve a poner el libro en estado disponible.

🔹 5. Listar libros

Muestra todos los libros almacenados, indicando si están disponibles o prestados.

🔹 6. Listar préstamos

Muestra todos los préstamos realizados, con sus fechas y si ya fueron devueltos.
🧩 Estructura del proyecto
📁 biblioteca/
│
├── main.py                # Archivo principal con el menú y funciones
├── README.md              # Documentación del proyecto
└── base_datos.sql         # Script SQL para crear las tablas
🗃️ Estructura de la base de datos
Base de datos: biblioteca
CREATE DATABASE biblioteca;
USE biblioteca;
Tabla: libros
CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  autor VARCHAR(100),
  anio INT,
  disponible BOOLEAN DEFAULT TRUE
);
Tabla: usuarios
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  tipo VARCHAR(50)
);
Tabla: prestamos
CREATE TABLE prestamos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT,
  id_libro INT,
  fecha_prestamo DATE,
  fecha_devolucion DATE,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
  FOREIGN KEY (id_libro) REFERENCES libros(id)
);
💻 Requisitos previos

Antes de ejecutar el programa, asegúrate de tener instalado:

Python 3.10 o superior

MySQL Server

Conector de MySQL para Python:
pip install mysql-connector-python
🚀 Ejecución del programa

Crea la base de datos en MySQL ejecutando el script base_datos.sql.

Verifica que las credenciales en el archivo principal sean correctas:
self.conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="biblioteca"
)
Ejecuta el programa desde la terminal:
python main.py
Usa el menú para interactuar con el sistema:
========= 📚 SISTEMA DE BIBLIOTECA =========
1. Registrar libro
2. Registrar usuario
3. Registrar préstamo
4. Devolver libro
5. Listar libros
6. Listar préstamos
0. Salir
🧠 Conceptos aplicados

Programación Orientada a Objetos (POO)

Clases: Libro, Usuario, Prestamo, ConexionBD

Encapsulamiento mediante atributos privados y métodos get/set

CRUD en base de datos MySQL

Manejo de conexiones y consultas SQL en Python

Interfaz de texto con menú interactivo
