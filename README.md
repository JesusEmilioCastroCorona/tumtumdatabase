<img width="1920" height="1080" alt="Captura de pantalla (13)" src="https://github.com/user-attachments/assets/df45d3fc-73e8-4193-8b9b-cd346f17022d" />

Sistema de Biblioteca en Python + MySQL
 Descripción
 Este proyecto es un **sistema de gestión de biblioteca** desarrollado en **Python** con conexión a
 una base de datos **MySQL**.
 Permite registrar libros, usuarios, préstamos y devoluciones, así como listar los libros y los préstamos
 activos.
 Funcionalidades principales- Registrar nuevos libros con título, autor y año.- Registrar usuarios con nombre y tipo (Alumno, Profesor, etc.).- Registrar préstamos de libros a usuarios.- Registrar devoluciones de libros prestados.- Listar todos los libros y su disponibilidad.- Listar todos los préstamos realizados.
 Clases principales- **ConexionBD**: Maneja la conexión con MySQL y las consultas SQL.- **Libro**: Representa un libro con atributos como título, autor, año y disponibilidad.- **Usuario**: Representa a un usuario con nombre y tipo.- **Prestamo**: Gestiona la información de los préstamos de libros.
 Estructura de la base de datos
 La base de datos se llama **biblioteca** y contiene las siguientes tablas:
 Tabla `libros`
 | Campo | Tipo | Descripción |
 |--------|------|-------------|
 | id | INT AUTO_INCREMENT | Identificador único |
 | titulo | VARCHAR(100) | Título del libro |
 | autor | VARCHAR(100) | Autor del libro |
 | anio | INT | Año de publicación |
 | disponible | BOOLEAN | Indica si el libro está disponible |
 Tabla `usuarios`
 | Campo | Tipo | Descripción |
 |--------|------|-------------|
 | id | INT AUTO_INCREMENT | Identificador único |
 | nombre | VARCHAR(100) | Nombre del usuario |
 | tipo | VARCHAR(50) | Tipo de usuario (Alumno, Profesor, etc.) |
 Tabla `prestamos`
 | Campo | Tipo | Descripción |
 |--------|------|-------------|
 | id | INT AUTO_INCREMENT | Identificador único |
 | id_usuario | INT | ID del usuario |
| id_libro | INT | ID del libro |
 | fecha_prestamo | DATE | Fecha del préstamo |
 | fecha_devolucion | DATE | Fecha de devolución (NULL si no se ha devuelto) |
 Requisitos- Python 3.10 o superior- MySQL Server- Librería `mysql-connector-python`
 Instalar dependencias:
 ```bash
 pip install mysql-connector-python
 ```
 Ejecución
 1. Crea la base de datos en MySQL con el nombre `biblioteca`.
 2. Crea las tablas siguiendo la estructura anterior.
 3. Ejecuta el programa:
 ```bash
 python biblioteca.py
