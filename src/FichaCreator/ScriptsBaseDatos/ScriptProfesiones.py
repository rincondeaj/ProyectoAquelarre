import sqlite3

# Crear o conectar a la base de datos SQLite
conexion = sqlite3.connect("BaseDatos/profesiones.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

COMPETENCIAS = [
   ("Alquimia", "Cultura"),
    ("Artesania", "Habilidad"),
    ("Astrologia", "Cultura"),
    ("Cabalgar", "Agilidad"),
    ("Cantar", "Comunicacion"),
    ("Comerciar", "Comunicacion"),
    ("ConducirCarro", "Habilidad"),
    ("ConAnimal", "Cultura"),
    ("ConAreaSlot1", "Cultura"),
    ("ConAreaNumSlot1", "Cultura"),
    ("ConAreaSlot2", "Cultura"),
    ("ConAreaNumSlot2", "Cultura"),
    ("ConMagico", "Cultura"),
    ("ConMineral", "Cultura"),
    ("ConVegetal", "Cultura"),
    ("Correr", "Agilidad"),
    ("Corte", "Comunicacion"),
    ("Degustar", "Percepcion"),
    ("Descubrir", "Percepcion"),
    ("Disfrazarse", "Comunicacion"),
    ("Elocuencia", "Comunicacion"),
    ("Empatia", "Percepcion"),
    ("Ensenar", "Comunicacion"),
    ("Escamotear", "Habilidad"),
    ("Escuchar", "Percepcion"),
    ("Esquivar", "Agilidad"),
    ("ForzarMecanismos", "Habilidad"),
    ("IdiomaSlot1", "Cultura"),
    ("IdiomaSlot2", "Cultura"),
    ("IdiomaSlot3", "Cultura"),
    ("IdiomaNumSlot1", "Cultura"),
    ("IdiomaNumSlot2", "Cultura"),
    ("IdiomaNumSlot3", "Cultura"),
    ("Juego", "Habilidad"),
    ("Lanzar", "Agilidad"),
    ("LeerEscribir", "Cultura"),
    ("Leyendas", "Cultura"),
    ("Mando", "Comunicacion"),
    ("Medicina", "Cultura"),
    ("Memoria", "Percepcion"),
    ("Musica", "Cultura"),
    ("Nadar", "Agilidad"),
    ("Navegar", "Habilidad"),
    ("Ocultar", "Habilidad"),
    ("Rastrear", "Percepcion"),
    ("Saltar", "Agilidad"),
    ("Sanar", "Habilidad"),
    ("Seduccion", "Aspecto"),
    ("Sigilo", "Agilidad"),
    ("Teologia", "Cultura"),
    ("Tormento", "Habilidad"),
    ("Trepar", "Agilidad"),
    ("CompetenciaAuxSlot1", "Neutral"),
    ("CompetenciaAuxSlot2", "Neutral"),
    ("CompetenciaAuxSlot3", "Neutral"),
    ("CompetenciaAuxSlot4", "Neutral"),
    ("CompetenciaAuxSlot5", "Neutral"),
    ("CompetenciaAuxNumSlot1", "Neutral"),
    ("CompetenciaAuxNumSlot2", "Neutral"),
    ("CompetenciaAuxNumSlot3", "Neutral"),
    ("CompetenciaAuxNumSlot4", "Neutral"),
    ("CompetenciaAuxNumSlot5", "Neutral"),
    ("Arcos", "Percepcion"),
    ("Ballestas", "Percepcion"),
    ("Cuchillos", "Habilidad"),
    ("Escudos", "Habilidad"),
    ("Espadas", "Habilidad"),
    ("Espadones", "Fuerza"),
    ("Hachas", "Fuerza"),
    ("Hondas", "Percepcion"),
    ("Lanzas", "Agilidad"),
    ("Mazas", "Fuerza"),
    ("Palos", "Agilidad"),
    ("Pelea", "Agilidad"),
    ("Latín", 'Lengua'),
    ("Árabe", 'Lengua'),
    ("Hebreo", 'Lengua'),
    ("Romance", 'Lengua'),
    ("Euskera", 'Lengua'),
    ("Castellano", 'Lengua'),
    ("Griego", 'Lengua')
]

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Profesiones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Fuerza INT NOT NULL,
        Agilidad INT NOT NULL,
        Habilidad INT NOT NULL,
        Resistencia INT NOT NULL,
        Percepcion INT NOT NULL,
        Comunicacion INT NOT NULL,
        Cultura INT NOT NULL,
        Aspecto INT NOT NULL,
        Suerte INT NOT NULL
    );         
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Competencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Caracteristica TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE Profesion_Competencia (
        profesion_id INTEGER,
        competencia_id INTEGER,
        tipo TEXT NOT NULL CHECK(tipo IN ('Primaria', 'Secundaria', 'Armas', 'Idiomas')),
        FOREIGN KEY (profesion_id) REFERENCES Profesiones(id),
        FOREIGN KEY (competencia_id) REFERENCES Competencias(id),
        PRIMARY KEY (profesion_id, competencia_id, tipo)  -- Una competencia puede ser de varios tipos
    );
''')

cursor.execute('''
    INSERT INTO Profesiones (Nombre, Fuerza, Agilidad, Habilidad, Resistencia, Percepcion, Comunicacion, Cultura, Aspecto, Suerte ) VALUES
        ('Alguacil',5,15,15,5,5,5,5,6,0),
        ('Almogávar',5,20,20,5,5,5,5,6,0),
        ('Alquimista',5,5,5,5,5,5,20,6,0),
        ('Ama',5,5,5,5,20,5,5,6,0),
        ('Artesano',5,5,20,5,15,5,5,6,0),
        ('Bandido',5,5,5,15,15,5,5,6,0),
        ('Barbero Cirujano',5,5,15,5,5,10,10,6,0),
        ('Brujo',5,5,5,5,5,5,15,6,0),
        ('Bufón',5,20,20,5,5,5,5,6,0),
        ('Caballero de Orden Militar',5,15,5,5,5,5,15,6,0),
        ('Cambista',5,5,10,5,10,5,15,6,0),
        ('Cazador',5,5,5,5,20,5,5,6,0),
        ('Clérigo',5,5,5,5,5,5,15,6,50),
        ('Comerciante',5,5,5,5,5,20,5,6,0),
        ('Cómico',5,5,5,5,5,20,5,6,0),
        ('Cortesano',5,5,5,5,15,15,5,6,0),
        ('Curandero',5,5,15,5,5,5,10,6,0),
        ('Derviche',5,15,5,5,5,5,20,6,0),
        ('Embaucador',5,10,5,5,5,15,5,6,0),
        ('Escriba',5,5,5,5,5,15,15,6,0),
        ('Ghazí',5,15,15,5,5,5,5,6,40),
        ('Goliardo',5,10,10,5,5,5,15,6,0),
        ('Infanzón',15,15,5,5,5,5,5,6,0),
        ('Juglar',5,15,5,5,5,20,10,6,0),
        ('Ladrón',5,15,20,5,5,5,5,6,0),
        ('Mago',5,5,5,5,15,5,20,6,0),
        ('Malsín',5,15,5,5,20,5,5,6,0),
        ('Marino',5,15,15,5,5,5,5,6,0),
        ('Médico',5,5,15,5,5,5,15,6,0),
        ('Mediero',5,5,5,5,5,15,15,6,0),
        ('Mendigo',5,5,5,5,5,5,5,6,0),
        ('Monje',5,5,5,5,5,5,15,6,45),
        ('Muccadim',15,5,5,5,5,5,10,6,0),
        ('Pardo',5,20,15,5,5,5,5,6,0),
        ('Pastor',5,15,5,5,20,5,5,6,0),
        ('Pirata',5,15,15,5,5,5,5,6,0),
        ('Qaína',5,15,5,5,5,15,5,6,0),
        ('Rabino',5,5,5,5,5,5,20,6,50),
        ('Ramera',5,5,5,5,5,5,5,17,0),
        ('Sacerdote',5,5,5,5,5,5,15,6,50),
        ('Siervo de Corte',5,15,15,5,5,5,5,6,0),
        ('Soldado',15,5,15,5,5,5,5,6,0),
        ('Trovador',5,5,5,5,5,15,15,6,0),
        ('Ulema',5,5,5,5,5,5,20,6,50);    
''')

cursor.executemany('''
    INSERT INTO Competencias (Nombre, Caracteristica) VALUES (?, ?)
''', COMPETENCIAS)

profesion_competencia_data = [
    (1, 10, 'Primaria'),
    (1, 12, 'Primaria'),
    (1, 16, 'Primaria'),
    (1, 25, 'Primaria'),
    (1, 63, 'Armas'),
    (1, 64, 'Armas'),
    (1, 65, 'Armas'),
    (1, 66, 'Armas'),
    (1, 69, 'Armas'),
    (1, 70, 'Armas'),
    (1, 71, 'Armas'),
    (1, 72, 'Armas'),
    (1, 73, 'Armas'),
    (1, 74, 'Armas'),
    (1, 19, 'Secundaria'),
    (1, 22, 'Secundaria'),
    (1, 38, 'Secundaria'),
    (1, 45, 'Secundaria'),
    (1, 49, 'Secundaria'),
    (1, 51, 'Secundaria'),
    (2, 49, 'Primaria'),
    (2, 66, 'Primaria'),
    (2, 26, 'Primaria'),
    (2, 63, 'Armas'),
    (2, 64, 'Armas'),
    (2, 65, 'Armas'),
    (2, 66, 'Armas'),
    (2, 69, 'Armas'),
    (2, 70, 'Armas'),
    (2, 71, 'Armas'),
    (2, 72, 'Armas'),
    (2, 73, 'Armas'),
    (2, 74, 'Armas'),
    (2, 16, 'Secundaria'),
    (2, 65, 'Secundaria'),
    (2, 19, 'Secundaria'),
    (2, 25, 'Secundaria'),
    (2, 45, 'Secundaria'),
    (2, 47, 'Secundaria'),
    (2, 51, 'Secundaria'),
    (3, 1, 'Primaria'),
    (3, 3, 'Primaria'),
    (3, 13, 'Primaria'),
    (3, 36, 'Primaria'),
    (3, 8, 'Secundaria'),
    (3, 14, 'Secundaria'),
    (3, 15, 'Secundaria'),
    (3, 22, 'Secundaria'),
    (3, 23, 'Secundaria'),
    (3, 75, 'Idiomas'),
    (3, 81, 'Idiomas'),
    (3, 47, 'Secundaria'),
    (4, 17, 'Primaria'),
    (4, 19, 'Primaria'),
    (4, 23, 'Primaria'),
    (4, 49, 'Primaria'),
    (4, 2, 'Secundaria'),
    (4, 15, 'Secundaria'),
    (4, 22, 'Secundaria'),
    (4, 25, 'Secundaria'),
    (4, 75, 'Idiomas'),
    (4, 76, 'Idiomas'),
    (4, 77, 'Idiomas'),
    (4, 78, 'Idiomas'),
    (4, 79, 'Idiomas'),
    (4, 80, 'Idiomas'),
    (4, 81, 'Idiomas'),
    (4, 38, 'Secundaria'),
    (4, 47, 'Secundaria'),
    (4, 40, 'Secundaria'),
    (5, 2, 'Primaria'),
    (5, 19, 'Primaria'),
    (5, 6, 'Primaria'),
    (5, 40, 'Primaria'),
    (5, 7, 'Secundaria'),
    (5, 10, 'Secundaria'),
    (5, 12, 'Secundaria'),
    (5, 65, 'Armas'),
    (5, 21, 'Secundaria'),
    (5, 22, 'Secundaria'),
    (5, 23, 'Secundaria'),
    (5, 25, 'Secundaria'),
    (5, 36, 'Secundaria'),
    (6, 19, 'Primaria'),
    (6, 49, 'Primaria'),
    (6, 51, 'Primaria'),
    (6, 63, 'Armas'),
    (6, 64, 'Armas'),
    (6, 65, 'Armas'),
    (6, 66, 'Armas'),
    (6, 69, 'Armas'),
    (6, 70, 'Armas'),
    (6, 71, 'Armas'),
    (6, 72, 'Armas'),
    (6, 73, 'Armas'),
    (6, 74, 'Armas'),
    (6, 10, 'Secundaria'),
    (6, 12, 'Secundaria'),
    (6, 22, 'Secundaria'),
    (6, 25, 'Secundaria'),
    (6, 35, 'Secundaria'),
    (6, 45, 'Secundaria'),
    (6, 52, 'Secundaria'),
    (7, 21, 'Primaria'),
    (7, 32, 'Primaria'),
    (7, 39, 'Primaria'),
    (7, 47, 'Primaria'),
    (7, 6, 'Secundaria'),
    (7, 7, 'Secundaria'),
    (7, 15, 'Secundaria'),
    (7, 16, 'Secundaria'),
    (7, 19, 'Secundaria'),
    (7, 36, 'Secundaria'),
    (7, 75, 'Idiomas'),
    (7, 76, 'Idiomas'),
    (7, 77, 'Idiomas'),
    (7, 78, 'Idiomas'),
    (7, 79, 'Idiomas'),
    (7, 80, 'Idiomas'),
    (7, 81, 'Idiomas'),
    (8, 1, 'Primaria'),
    (8, 3, 'Primaria'),
    (8, 13, 'Primaria'),
    (8, 15, 'Primaria'),
    (8, 8, 'Secundaria'),
    (8, 14, 'Secundaria'),
    (8, 19, 'Secundaria'),
    (8, 22, 'Secundaria'),
    (8, 23, 'Secundaria'),
    (8, 37, 'Secundaria'),
    (8, 39, 'Secundaria'),
    (8, 47, 'Secundaria'),
    (9, 20, 'Primaria'),
    (9, 21, 'Primaria'),
    (9, 24, 'Primaria'),
    (9, 46, 'Primaria'),
    (9, 20, 'Secundaria'),
    (9, 16, 'Secundaria'),
    (9, 17, 'Secundaria'),
    (9, 34, 'Secundaria'),
    (9, 35, 'Secundaria'),
    (9, 41, 'Secundaria'),
    (9, 44, 'Secundaria'),
    (9, 49, 'Secundaria'),
    (9, 52, 'Secundaria'),
    (10, 4, 'Primaria'),
    (10, 50, 'Primaria'),
    (10, 64, 'Armas'),
    (10, 65, 'Armas'),
    (10, 66, 'Armas'),
    (10, 67, 'Armas'),
    (10, 68, 'Armas'),
    (10, 71, 'Armas'),
    (10, 74, 'Armas'),
    (10, 19, 'Secundaria'),
    (10, 21, 'Secundaria'),
    (10, 22, 'Secundaria'),
    (10, 25, 'Secundaria'),
    (10, 26, 'Secundaria'),
    (10, 75, 'Idiomas'),
    (10, 36, 'Secundaria'),
    (10, 38, 'Secundaria'),
    (11, 1, 'Primaria'),
    (11, 6, 'Primaria'),
    (11, 14, 'Primaria'),
    (11, 21, 'Primaria'),
    (11, 2, 'Secundaria'),
    (11, 65, 'Armas'),
    (11, 19, 'Secundaria'),
    (11, 22, 'Secundaria'),
    (11, 75, 'Idiomas'),
    (11, 76, 'Idiomas'),
    (11, 77, 'Idiomas'),
    (11, 78, 'Idiomas'),
    (11, 79, 'Idiomas'),
    (11, 80, 'Idiomas'),
    (11, 81, 'Idiomas'),
    (11, 36, 'Secundaria'),
    (11, 40, 'Secundaria'),
    (11, 44, 'Secundaria'),
    (11, 47, 'Secundaria'),
    (11, 49, 'Secundaria'),
    (11, 51, 'Secundaria'),
    (12, 63, 'Primaria'),
    (12, 25, 'Primaria'),
    (12, 45, 'Primaria'),
    (12, 49, 'Primaria'),
    (12, 4, 'Secundaria'),
    (12, 8, 'Secundaria'),
    (12, 10, 'Secundaria'),
    (12, 12, 'Secundaria'),
    (12, 15, 'Secundaria'),
    (12, 19, 'Secundaria'),
    (12, 35, 'Secundaria'),
    (12, 52, 'Secundaria'),
    (12, 65, 'Armas'),
    (13, 21, 'Primaria'),
    (13, 36, 'Primaria'),
    (13, 50, 'Primaria'),
    (13, 75, 'Idiomas'),
    (13, 17, 'Secundaria'),
    (13, 19, 'Secundaria'),
    (13, 22, 'Secundaria'),
    (13, 23, 'Secundaria'),
    (13, 25, 'Secundaria'),
    (13, 81, 'Idiomas'),
    (13, 40, 'Secundaria'),
    (13, 64, 'Armas'),
    (13, 65, 'Armas'),
    (13, 66, 'Armas'),
    (13, 67, 'Armas'),
    (13, 68, 'Armas'),
    (13, 71, 'Armas'),
    (13, 74, 'Armas'),
    (14, 6, 'Primaria'),
    (14, 21, 'Primaria'),
    (14, 22, 'Primaria'),
    (14, 75, 'Idiomas'),
    (14, 76, 'Idiomas'),
    (14, 77, 'Idiomas'),
    (14, 78, 'Idiomas'),
    (14, 79, 'Idiomas'),
    (14, 80, 'Idiomas'),
    (14, 81, 'Idiomas'),
    (14, 7, 'Secundaria'),
    (14, 19, 'Secundaria'),
    (14, 43, 'Secundaria'),
    (14, 25, 'Secundaria'),
    (14, 36, 'Secundaria'),
    (14, 42, 'Secundaria'),
    (14, 44, 'Secundaria'),
    (15, 20, 'Primaria'),
    (15, 21, 'Primaria'),
    (15, 22, 'Primaria'),
    (15, 40, 'Primaria'),
    (15, 7, 'Secundaria'),
    (15, 23, 'Secundaria'),
    (15, 24, 'Secundaria'),
    (15, 25, 'Secundaria'),
    (15, 37, 'Secundaria'),
    (15, 50, 'Secundaria'),
    (15, 75, 'Idiomas'),
    (15, 76, 'Idiomas'),
    (15, 77, 'Idiomas'),
    (15, 78, 'Idiomas'),
    (15, 79, 'Idiomas'),
    (15, 80, 'Idiomas'),
    (15, 81, 'Idiomas'),
    (15, 65, 'Armas'),
    (16, 17, 'Primaria'),
    (16, 21, 'Primaria'),
    (16, 22, 'Primaria'),
    (16, 48, 'Primaria'),
    (16, 4, 'Secundaria'),
    (16, 6, 'Secundaria'),
    (16, 19, 'Secundaria'),
    (16, 25, 'Secundaria'),
    (16, 36, 'Secundaria'),
    (16, 49, 'Secundaria'),
    (16, 64, 'Armas'),
    (16, 65, 'Armas'),
    (16, 66, 'Armas'),
    (16, 67, 'Armas'),
    (16, 68, 'Armas'),
    (16, 71, 'Armas'),
    (16, 74, 'Armas'),
    (17, 1, 'Primaria'),
    (17, 13, 'Primaria'),
    (17, 22, 'Primaria'),
    (17, 47, 'Primaria'),
    (17, 3, 'Secundaria'),
    (17, 8, 'Secundaria'),
    (17, 19, 'Secundaria'),
    (17, 14, 'Secundaria'),
    (17, 15, 'Secundaria'),
    (17, 37, 'Secundaria'),
    (17, 39, 'Secundaria'),
    (18, 21, 'Primaria'),
    (18, 22, 'Primaria'),
    (18, 36, 'Primaria'),
    (18, 50, 'Primaria'),
    (18, 13, 'Secundaria'),
    (18, 19, 'Secundaria'),
    (18, 25, 'Secundaria'),
    (18, 26, 'Secundaria'),
    (18, 23, 'Secundaria'),
    (18, 37, 'Secundaria'),
    (18, 40, 'Secundaria'),
    (18, 47, 'Secundaria'),
    (19, 6, 'Primaria'),
    (19, 7, 'Primaria'),
    (19, 21, 'Primaria'),
    (19, 22, 'Primaria'),
    (19, 1, 'Secundaria'),
    (19, 15, 'Secundaria'),
    (19, 16, 'Secundaria'),
    (19, 20, 'Secundaria'),
    (19, 24, 'Secundaria'),
    (19, 26, 'Secundaria'),
    (19, 75, 'Idiomas'),
    (19, 76, 'Idiomas'),
    (19, 77, 'Idiomas'),
    (19, 78, 'Idiomas'),
    (19, 79, 'Idiomas'),
    (19, 80, 'Idiomas'),
    (19, 81, 'Idiomas'),
    (19, 65, 'Armas'),
    (20, 6, 'Primaria'),
    (20, 36, 'Primaria'),
    (20, 40, 'Primaria'),
    (20, 75, 'Idiomas'),
    (20, 76, 'Idiomas'),
    (20, 77, 'Idiomas'),
    (20, 78, 'Idiomas'),
    (20, 79, 'Idiomas'),
    (20, 80, 'Idiomas'),
    (20, 81, 'Idiomas'),
    (20, 19, 'Secundaria'),
    (20, 21, 'Secundaria'),
    (20, 22, 'Secundaria'),
    (20, 23, 'Secundaria'),
    (20, 25, 'Secundaria'),
    (20, 49, 'Secundaria'),
    (21, 4, 'Primaria'),
    (21, 50, 'Primaria'),
    (21, 63, 'Armas'),
    (21, 64, 'Armas'),
    (21, 65, 'Armas'),
    (21, 66, 'Armas'),
    (21, 69, 'Armas'),
    (21, 70, 'Armas'),
    (21, 71, 'Armas'),
    (21, 72, 'Armas'),
    (21, 73, 'Armas'),
    (21, 74, 'Armas'),
    (21, 19, 'Secundaria'),
    (21, 22, 'Secundaria'),
    (21, 23, 'Secundaria'),
    (21, 66, 'Armas'),
    (21, 26, 'Secundaria'),
    (21, 36, 'Secundaria'),
    (21, 38, 'Secundaria'),
    (21, 47, 'Secundaria'),
    (21, 51, 'Secundaria'),
    (22, 5, 'Primaria'),
    (22, 24, 'Primaria'),
    (22, 36, 'Primaria'),
    (22, 48, 'Primaria'),
    (22, 16, 'Secundaria'),
    (22, 26, 'Secundaria'),
    (22, 34, 'Secundaria'),
    (22, 50, 'Secundaria'),
    (22, 74, 'Armas'),
    (22, 75, 'Idiomas'),
    (23, 4, 'Primaria'),
    (23, 38, 'Primaria'),
    (23, 63, 'Armas'),
    (23, 64, 'Armas'),
    (23, 65, 'Armas'),
    (23, 66, 'Armas'),
    (23, 69, 'Armas'),
    (23, 70, 'Armas'),
    (23, 71, 'Armas'),
    (23, 72, 'Armas'),
    (23, 73, 'Armas'),
    (23, 74, 'Armas'),
    (23, 19, 'Secundaria'),
    (23, 25, 'Secundaria'),
    (23, 26, 'Secundaria'),
    (23, 34, 'Secundaria'),
    (23, 51, 'Secundaria'),
    (24, 5, 'Primaria'),
    (24, 21, 'Primaria'),
    (24, 24, 'Primaria'),
    (24, 41, 'Primaria'),
    (24, 16, 'Secundaria'),
    (24, 26, 'Secundaria'),
    (24, 36, 'Secundaria'),
    (24, 37, 'Secundaria'),
    (24, 46, 'Secundaria'),
    (24, 49, 'Secundaria'),
    (24, 74, 'Armas'),
    (25, 16, 'Primaria'),
    (25, 24, 'Primaria'),
    (25, 26, 'Primaria'),
    (25, 52, 'Primaria'),
    (25, 6, 'Secundaria'),
    (25, 19, 'Secundaria'),
    (25, 20, 'Secundaria'),
    (25, 25, 'Secundaria'),
    (25, 27, 'Secundaria'),
    (25, 35, 'Secundaria'),
    (25, 49, 'Secundaria'),
    (25, 63, 'Armas'),
    (25, 65, 'Armas'),
    (25, 69, 'Armas'),
    (25, 70, 'Armas'),
    (25, 71, 'Armas'),
    (25, 72, 'Armas'),
    (25, 73, 'Armas'),
    (25, 74, 'Armas'),
    (26, 13, 'Primaria'),
    (26, 21, 'Primaria'),
    (26, 36, 'Primaria'),
    (26, 50, 'Primaria'),
    (26, 1, 'Secundaria'),
    (26, 3, 'Secundaria'),
    (26, 8, 'Secundaria'),
    (26, 14, 'Secundaria'),
    (26, 15, 'Secundaria'),
    (26, 23, 'Secundaria'),
    (26, 39, 'Secundaria'),
    (26, 40, 'Secundaria'),
    (27, 12, 'Primaria'),
    (27, 14, 'Primaria'),
    (27, 25, 'Primaria'),
    (27, 27, 'Primaria'),
    (27, 49, 'Primaria'),
    (27, 6, 'Secundaria'),
    (27, 16, 'Secundaria'),
    (27, 19, 'Secundaria'),
    (27, 22, 'Secundaria'),
    (27, 4, 'Secundaria'),
    (27, 46, 'Secundaria'),
    (27, 52, 'Secundaria'),
    (27, 63, 'Armas'),
    (27, 65, 'Armas'),
    (27, 69, 'Armas'),
    (27, 70, 'Armas'),
    (27, 71, 'Armas'),
    (27, 72, 'Armas'),
    (27, 73, 'Armas'),
    (27, 74, 'Armas'),
    (28, 19, 'Primaria'),
    (28, 42, 'Primaria'),
    (28, 43, 'Primaria'),
    (28, 49, 'Primaria'),
    (28, 3, 'Secundaria'),
    (28, 34, 'Secundaria'),
    (28, 40, 'Secundaria'),
    (28, 75, 'Idiomas'),
    (28, 76, 'Idiomas'),
    (28, 77, 'Idiomas'),
    (28, 78, 'Idiomas'),
    (28, 79, 'Idiomas'),
    (28, 80, 'Idiomas'),
    (28, 81, 'Idiomas'),
    (28, 47, 'Secundaria'),
    (28, 48, 'Secundaria'),
    (28, 63, 'Armas'),
    (28, 64, 'Armas'),
    (28, 65, 'Armas'),
    (28, 69, 'Armas'),
    (28, 70, 'Armas'),
    (28, 71, 'Armas'),
    (28, 72, 'Armas'),
    (28, 73, 'Armas'),
    (28, 74, 'Armas'),
    (29, 15, 'Primaria'),
    (29, 22, 'Primaria'),
    (29, 39, 'Primaria'),
    (29, 47, 'Primaria'),
    (29, 1, 'Secundaria'),
    (29, 8, 'Secundaria'),
    (29, 14, 'Secundaria'),
    (29, 19, 'Secundaria'),
    (29, 21, 'Secundaria'),
    (29, 36, 'Secundaria'),
    (29, 40, 'Secundaria'),
    (29, 63, 'Armas'),
    (29, 65, 'Armas'),
    (29, 69, 'Armas'),
    (29, 70, 'Armas'),
    (29, 71, 'Armas'),
    (29, 72, 'Armas'),
    (29, 73, 'Armas'),
    (29, 74, 'Armas'),
    (30, 6, 'Primaria'),
    (30, 12, 'Primaria'),
    (30, 14, 'Primaria'),
    (30, 21, 'Primaria'),
    (30, 22, 'Primaria'),
    (30, 20, 'Secundaria'),
    (30, 24, 'Secundaria'),
    (30, 26, 'Secundaria'),
    (30, 36, 'Secundaria'),
    (30, 38, 'Secundaria'),
    (30, 49, 'Secundaria'),
    (30, 51, 'Secundaria'),
    (30, 63, 'Armas'),
    (30, 65, 'Armas'),
    (30, 69, 'Armas'),
    (30, 70, 'Armas'),
    (30, 71, 'Armas'),
    (30, 72, 'Armas'),
    (30, 73, 'Armas'),
    (30, 74, 'Armas'),
    (31, 21, 'Primaria'),
    (31, 22, 'Primaria'),
    (31, 24, 'Primaria'),
    (31, 40, 'Primaria'),
    (31, 2, 'Secundaria'),
    (31, 6, 'Secundaria'),
    (31, 34, 'Secundaria'),
    (31, 75, 'Idiomas'),
    (31, 76, 'Idiomas'),
    (31, 77, 'Idiomas'),
    (31, 78, 'Idiomas'),
    (31, 79, 'Idiomas'),
    (31, 80, 'Idiomas'),
    (31, 81, 'Idiomas'),
    (31, 44, 'Secundaria'),
    (31, 49, 'Secundaria'),
    (31, 74, 'Armas'),
    (31, 63, 'Armas'),
    (31, 65, 'Armas'),
    (31, 69, 'Armas'),
    (31, 70, 'Armas'),
    (31, 71, 'Armas'),
    (31, 72, 'Armas'),
    (31, 73, 'Armas'),
    (31, 74, 'Armas'),
    (32, 23, 'Primaria'),
    (32, 36, 'Primaria'),
    (32, 50, 'Primaria'),
    (32, 75, 'Idiomas'),
    (32, 5, 'Secundaria'),
    (32, 19, 'Secundaria'),
    (32, 21, 'Secundaria'),
    (32, 22, 'Secundaria'),
    (32, 25, 'Secundaria'),
    (32, 40, 'Secundaria'),
    (32, 76, 'Idiomas'),
    (32, 81, 'Idiomas'),
    (33, 22, 'Primaria'),
    (33, 50, 'Primaria'),
    (33, 74, 'Armas'),
    (33, 63, 'Armas'),
    (33, 65, 'Armas'),
    (33, 69, 'Armas'),
    (33, 70, 'Armas'),
    (33, 71, 'Armas'),
    (33, 72, 'Armas'),
    (33, 73, 'Armas'),
    (33, 16, 'Secundaria'),
    (33, 19, 'Secundaria'),
    (33, 25, 'Secundaria'),
    (33, 26, 'Secundaria'),
    (33, 38, 'Secundaria'),
    (33, 46, 'Secundaria'),
    (33, 47, 'Secundaria'),
    (33, 51, 'Secundaria'),
    (34, 4, 'Primaria'),
    (34, 19, 'Primaria'),
    (34, 38, 'Primaria'),
    (34, 63, 'Armas'),
    (34, 64, 'Armas'),
    (34, 65, 'Armas'),
    (34, 69, 'Armas'),
    (34, 70, 'Armas'),
    (34, 71, 'Armas'),
    (34, 72, 'Armas'),
    (34, 73, 'Armas'),
    (34, 74, 'Armas'),
    (34, 6, 'Secundaria'),
    (34, 10, 'Secundaria'),
    (34, 12, 'Secundaria'),
    (34, 35, 'Secundaria'),
    (34, 75, 'Idiomas'),
    (34, 76, 'Idiomas'),
    (34, 77, 'Idiomas'),
    (34, 78, 'Idiomas'),
    (34, 79, 'Idiomas'),
    (34, 80, 'Idiomas'),
    (34, 81, 'Idiomas'),
    (34, 45, 'Secundaria'),
    (34, 47, 'Secundaria'),
    (34, 49, 'Secundaria'),
    (34, 51, 'Secundaria'),
    (35, 8, 'Primaria'),
    (35, 19, 'Primaria'),
    (35, 25, 'Primaria'),
    (35, 45, 'Primaria'),
    (35, 2, 'Secundaria'),
    (35, 3, 'Secundaria'),
    (35, 16, 'Secundaria'),
    (35, 70, 'Armas'),
    (35, 35, 'Secundaria'),
    (35, 46, 'Secundaria'),
    (35, 52, 'Secundaria'),
    (35, 73, 'Armas'),
    (36, 19, 'Primaria'),
    (36, 42, 'Primaria'),
    (36, 43, 'Primaria'),
    (36, 63, 'Armas'),
    (36, 64, 'Armas'),
    (36, 65, 'Armas'),
    (36, 69, 'Armas'),
    (36, 70, 'Armas'), 
    (36, 71, 'Armas'), 
    (36, 72, 'Armas'), 
    (36, 73, 'Armas'), 
    (36, 74, 'Armas'),
    (36, 3, 'Secundaria'),
    (36, 34, 'Secundaria'),
    (36, 35, 'Secundaria'),
    (36, 47, 'Secundaria'),
    (36, 48, 'Secundaria'),
    (36, 52, 'Secundaria'),
    (36, 75, 'Idiomas'),
    (36, 76, 'Idiomas'),
    (36, 77, 'Idiomas'),
    (36, 78, 'Idiomas'),
    (36, 79, 'Idiomas'),
    (36, 80, 'Idiomas'),
    (36, 81, 'Idiomas'),
    (37, 5, 'Primaria'),
    (37, 21, 'Primaria'),
    (37, 41, 'Primaria'),
    (37, 48, 'Primaria'),
    (37, 17, 'Secundaria'),
    (37, 22, 'Secundaria'),
    (37, 37, 'Secundaria'),
    (37, 40, 'Secundaria'),
    (37, 44, 'Secundaria'),
    (37, 47, 'Secundaria'),
    (37, 49, 'Secundaria'),
    (37, 75, 'Idiomas'),
    (37, 76, 'Idiomas'),
    (37, 77, 'Idiomas'),
    (37, 78, 'Idiomas'),
    (37, 79, 'Idiomas'),
    (37, 80, 'Idiomas'),
    (37, 81, 'Idiomas'),
    (38, 21, 'Primaria'),
    (38, 36, 'Primaria'),
    (38, 50, 'Primaria'),
    (38, 77, 'Idiomas'),
    (38, 3, 'Secundaria'),
    (38, 22, 'Secundaria'),
    (38, 23, 'Secundaria'),
    (38, 25, 'Secundaria'),
    (38, 40, 'Secundaria'),
    (38, 49, 'Secundaria'),
    (38, 75, 'Idiomas'),
    (38, 76, 'Idiomas'),
    (39, 21, 'Primaria'),
    (39, 24, 'Primaria'),
    (39, 48, 'Primaria'),
    (39, 49, 'Primaria'),
    (39, 6, 'Secundaria'),
    (39, 16, 'Secundaria'),
    (39, 19, 'Secundaria'),
    (39, 22, 'Secundaria'),
    (39, 27, 'Secundaria'),
    (39, 34, 'Secundaria'),
    (39, 44, 'Secundaria'),
    (39, 63, 'Armas'),
    (39, 65, 'Armas'),
    (39, 69, 'Armas'),
    (39, 70, 'Armas'), 
    (39, 71, 'Armas'), 
    (39, 72, 'Armas'), 
    (39, 73, 'Armas'), 
    (39, 74, 'Armas'),
    (40, 21, 'Primaria'),
    (40, 36, 'Primaria'),
    (40, 50, 'Primaria'),
    (40, 75, 'Idiomas'),
    (40, 5, 'Secundaria'),
    (40, 10, 'Secundaria'),
    (40, 12, 'Secundaria'),
    (40, 19, 'Secundaria'),
    (40, 22, 'Secundaria'),
    (40, 23, 'Secundaria'),
    (40, 25, 'Secundaria'),
    (40, 38, 'Secundaria'),
    (40, 40, 'Secundaria'),
    (41, 2, 'Primaria'),
    (41, 7, 'Primaria'),
    (41, 15, 'Primaria'),
    (41, 49, 'Primaria'),
    (41, 6, 'Secundaria'),
    (41, 16, 'Secundaria'),
    (41, 17, 'Secundaria'),
    (41, 18, 'Secundaria'),
    (41, 25, 'Secundaria'),
    (41, 34, 'Secundaria'),
    (41, 46, 'Secundaria'),
    (41, 63, 'Armas'),
    (41, 65, 'Armas'),
    (41, 69, 'Armas'),
    (41, 70, 'Armas'), 
    (41, 71, 'Armas'), 
    (41, 72, 'Armas'), 
    (41, 73, 'Armas'), 
    (41, 74, 'Armas'),
    (42, 4, 'Primaria'),
    (42, 64, 'Armas'),
    (42, 66, 'Armas'),
    (42, 63, 'Armas'),
    (42, 65, 'Armas'),
    (42, 69, 'Armas'),
    (42, 70, 'Armas'), 
    (42, 71, 'Armas'), 
    (42, 72, 'Armas'), 
    (42, 73, 'Armas'), 
    (42, 74, 'Armas'),
    (42, 7, 'Secundaria'),
    (42, 19, 'Secundaria'),
    (42, 26, 'Secundaria'),
    (42, 47, 'Secundaria'),
    (42, 49, 'Secundaria'),
    (42, 51, 'Secundaria'),
    (43, 21, 'Primaria'),
    (43, 36, 'Primaria'),
    (43, 41, 'Primaria'),
    (43, 48, 'Primaria'),
    (43, 4, 'Secundaria'),
    (43, 5, 'Secundaria'),
    (43, 17, 'Secundaria'),
    (43, 22, 'Secundaria'),
    (43, 37, 'Secundaria'),
    (43, 40, 'Secundaria'),
    (43, 49, 'Secundaria'),
    (43, 64, 'Armas'),
    (43, 65, 'Armas'),
    (43, 66, 'Armas'),
    (43, 67, 'Armas'),
    (43, 68, 'Armas'),
    (43, 71, 'Armas'),
    (43, 74, 'Armas'),
    (44, 36, 'Primaria'),
    (44, 40, 'Primaria'),
    (44, 50, 'Primaria'),
    (44, 76, 'Idiomas'),
    (44, 17, 'Secundaria'),
    (44, 19, 'Secundaria'),
    (44, 21, 'Secundaria'),
    (44, 22, 'Secundaria'),
    (44, 23, 'Secundaria'),
    (44, 25, 'Secundaria'),
    (44, 75, 'Idiomas'),
    (44, 77, 'Idiomas'),
    (44, 78, 'Idiomas'),
    (44, 79, 'Idiomas'),
    (44, 80, 'Idiomas'),
    (44, 81, 'Idiomas'),
    (44, 64, 'Armas'),
    (44, 65, 'Armas'),
    (44, 66, 'Armas'),
    (44, 67, 'Armas'),
    (44, 68, 'Armas'),
    (44, 71, 'Armas'),
    (44, 74, 'Armas'),
]

# Eliminar duplicados
profesion_competencia_data = list(set(profesion_competencia_data))

# Insertar los datos únicos en la tabla
cursor.executemany('''
    INSERT INTO Profesion_Competencia (profesion_id, competencia_id, tipo) VALUES (?, ?, ?)
''', profesion_competencia_data)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada y tabla 'Armas' configurada correctamente.")