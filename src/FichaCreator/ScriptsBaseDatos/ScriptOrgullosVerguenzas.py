import sqlite3

# Crear o conectar a la base de datos SQLite
conexion = sqlite3.connect("BaseDatos/OrgullosVerguenzas")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orgullos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Puntos INTEGER NOT NULL
    );         
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Verguenzas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Puntos INTEGER NOT NULL
    );         
''')


Orgullos = [
    ('Adiestrado para el combate', 2),
    ('Aficcionado a la caza', 2),
    ('Ágil', 2),
    ('Alto', 1),
    ('Ambidextro', 2),
    ('Amistad', 2),
    ('Caractertística Desarrollada', 1),
    ('Carisma con los animales', 1),
    ('Cautivador', 1),
    ('Clase social alta', 2),
    ('Comprensivo', 1),
    ('Conocimientos Arcanos', 2),
    ('Creencias firmes', 2),
    ('Criado en el campo', 1),
    ('Criado en la costa', 2),
    ('Dedos ligeros', 1),
    ('Don de lenguas', 1),
    ('Educación Alquímica', 1),
    ('Eduación Arcana', 1),
    ('Educación Religiosa', 2),
    ('Estudiante ejemplar', 2),
    ('Heredero', 1),
    ('Hermosura', 2),
    ('Imitador', 1),
    ('Lider', 1),
    ('Literato', 1),
    ('Locuaz', 1),
    ('Marrullero', 1),
    ('Mascota', 2),
    ('Memoria prodigiosa', 1),
    ('Pedagogo', 1),
    ('Persona del mundo', 1),
    ('Posesiones', 2),
    ('Reflejos felinos', 2),
    ('Reliquia Arcana', 2),
    ('Resistencia Natural', 2),
    ('Sanador', 2),
    ('Sentido de la orientación', 1),
    ('Sentidos desarrollados', 1),
    ('Sexto sentido', 2),
    ('Sigiloso', 1),
    ('Valentía', 2),
    ('Versado en leyendas', 1),
    ('Voz prodigiosa', 1)
]

Verguenzas = [
    ('Antipatía Animal', 2),
    ('Bajito', 1),
    ('Cándido', 1),
    ('Característica debilitada', 2),
    ('Clase social baja', 2),
    ('Cobardía', 2),
    ('Compañero de infortunios', 2),
    ('Conocimientos Arcanos insuficientes', 2),
    ('Defecto físico', 2),
    ('Delicado', 2),
    ('Desheredado', 1),
    ('Despistado', 1),
    ('Dolencia', 2),
    ('Enjuto', 1),
    ('Extranjero', 1),
    ('Fealdad', 2),
    ('Hechizos extraños', 2),
    ('Honor del guerrero', 2),
    ('Honrado', 2),
    ('Intransigente', 1),
    ('Lozanía', 2),
    ('Maldito por dios', 3),
    ('Mugriento', 2),
    ('Orondo', 3),
    ('Pobre', 1),
    ('Reliquia familiar', 1),
    ('Secreto', 2),
    ('Tarado', 2),
    ('Vejez', 2)
]
cursor.executemany('''
    INSERT INTO Orgullos (Nombre, Puntos) VALUES (?, ?)
''', Orgullos)

cursor.executemany('''
    INSERT INTO Verguenzas (Nombre, Puntos) VALUES (?, ?)
''', Verguenzas)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada y tabla 'Orgullos' configurada correctamente.")