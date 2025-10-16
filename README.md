<img width="1920" height="1080" alt="Captura de pantalla (13)" src="https://github.com/user-attachments/assets/df45d3fc-73e8-4193-8b9b-cd346f17022d" />

📚 Sistema de Biblioteca con Conexión a MySQL
✨ Descripción
Este proyecto consiste en un Sistema de Biblioteca desarrollado en Python utilizando Programación Orientada a Objetos (POO) y encapsulamiento, con persistencia de datos mediante una base de datos MySQL. El sistema permite gestionar:

📖 Libros
👤 Usuarios
📝 Préstamos
Se implementa un menú por terminal que permite registrar, listar y consultar información, garantizando que los datos se almacenen de manera segura y escalable.

⭐ Características
🔒 Encapsulamiento: Las clases Libro, Usuario y Prestamo tienen atributos privados y métodos get y set.
💾 Persistencia de datos: Toda la información se guarda en MySQL.
✅ Validaciones: Verifica la disponibilidad de libros antes de registrar un préstamo.
🖥️ Interfaz por terminal: Menú interactivo para administrar la biblioteca.
🛡️ Registro de operaciones: Uso de consultas parametrizadas para evitar inyecciones SQL y garantizar integridad.
🛠️ Tecnologías
🐍 Python 3.x
🗄️ MySQL
📦 Librería mysql-connector-python
📂 Estructura de la Base de Datos
📖 Tablas
libros

Campo	Tipo	Descripción
id	INT	Primary Key, auto_increment
titulo	VARCHAR(100)	Título del libro
autor	VARCHAR(100)	Autor del libro
anio	INT	Año de publicación
disponible	BOOLEAN	Disponibilidad del libro
usuarios

Campo	Tipo	Descripción
id	INT	Primary Key, auto_increment
nombre	VARCHAR(100)	Nombre del usuario
tipo	VARCHAR(50)	Tipo de usuario
prestamos

Campo	Tipo	Descripción
id	INT	Primary Key, auto_increment
id_usuario	INT	Foreign Key → usuarios(id)
id_libro	INT	Foreign Key → libros(id)
fecha_prestamo	DATE	Fecha de préstamo
fecha_devolucion	DATE	Fecha de devolución
Kevin
image
⚡ Instalación
Clonar el repositorio:
git clone https://github.com/tu_usuario/sistema-biblioteca.git
cd sistema-biblioteca
Instalar dependencias:
pip install mysql-connector-python
Crear la base de datos en MySQL:
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    anio INT,
    disponible BOOLEAN
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);
Configurar el archivo Base de datos.py con los datos de tu conexión MySQL.
🚀 Uso
Ejecutar el script principal:
python "Base de datos.py"
Seguir las opciones del menú:
📖 Registrar libro
👤 Registrar usuario
📝 Registrar préstamo (verifica disponibilidad)
📚 Listar libros
🧑‍💼 Listar usuarios
🔍 Consultar préstamos
🔄 Devolver libro
Los datos se guardan automáticamente en MySQL.
🧪 Datos de prueba
El proyecto incluye 5 libros, 5 usuarios y 5 préstamos de ejemplo para probar el sistema.

✨ Mejoras implementadas respecto al proyecto original
🔒 Encapsulamiento completo de las clases.
🛡️ Uso de consultas parametrizadas para mayor seguridad.
✅ Validación de disponibilidad antes de registrar préstamos.
🔄 Registro de devoluciones de libros.
🖥️ Menú interactivo con mensajes claros de éxito y error.
