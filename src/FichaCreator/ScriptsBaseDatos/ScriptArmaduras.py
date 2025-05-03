import sqlite3

# Crear o conectar a la base de datos SQLite
conexion = sqlite3.connect("BaseDatos/armaduras.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Armaduras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Precio INTEGER NOT NULL,
        Descripcion TEXT NOT NULL,
        Tipo TEXT NOT NULL,
        Proteccion TEXT NOT NULL,
        Resistencia TEXT NOT NULL,
        Localizaciones TEXT NOT NULL
    );         
''')

cursor.execute('''
    INSERT INTO Armaduras (Nombre, Precio, Descripcion, Tipo, Proteccion, Resistencia, Localizaciones) VALUES
    ('Pelliza de Piel', 108, 'Prenda de abrigo fabricada con pieles de animales sin curtir', 'Blanda', '1', '15', 'Pecho y abdomen'),
    ('Ropas Gruesas', 216, 'Ropas de abrigo con lana, pieles, vellones o una mezcla de todo ello', 'Blanda', '1', '30', 'Todo excepto cabeza'),
    ('Brazales', 48, 'Protección de cuero para los antebrazos, muy usado por arqueros', 'Ligera', '2', '10', 'Brazos'),
    ('Gambesón', 288, 'Túnica de cuero curtido o tela rellena de retales o pelo de caballo', 'Ligera', '2', '50', 'Todo excepto cabeza'),
    ('Gambesón Reforzado', 432, 'Gambesón con añadidos de lona rígida, cuero crudo e incluso metal', 'Ligera', '3', '75', 'Todo excepto cabeza'),
    ('Grebas de Cuero', 48, 'Protección de cuero para las tibias y espinillas', 'Ligera', '2', '15', 'Piernas'),
    ('Vélinez', 288, 'Jubón de cuero', 'Ligera', '2', '25', 'Pecho y abdomen'),
    ('Coraza Corta', 648, 'Armadura nazarí de metal para pecho y abdomen', 'Metálica', '6', '125', 'Pecho y abdomen'),
    ('Cota de Placas', 1620, 'Láminas de anillas reforzadas con láminas de metal', 'Metálica', '6', '150', 'Todo excepto cabeza'),
    ('Grebas de Metal', 142, 'Grebas fabricadas directamente en metal', 'Metálica', '4', '40', 'Piernas'),
    ('Loriga de Malla', 900, 'Cota de malla flexible', 'Metálica', '5', '125', 'Todo excepto cabeza'),
    ('Arnés', 2700, 'Coraza completa, muy pesada, formada por numerosas piezas de metal', 'Completa', '8', '300', 'Todo excepto cabeza'),
    ('Bacinete', 108, 'Casco de metal sin visera ni gola', 'Casco', '4', '40', 'Cabeza'),
    ('Capacete', 36, 'Casco ligero de protección básica', 'Casco', '2', '20', 'Cabeza'),
    ('Celada', 180, 'Yelmo que deja la parte inferior de la cara al descubierto', 'Casco', '6', '80', 'Cabeza'),
    ('Yelmo', 252, 'Casco que otorga una protección completa en toda la cabeza', 'Casco', '8', '100', 'Cabeza'),
    ('Bardas', 6840, 'Armadura para caballería pesada', 'Animal', '5', '150', 'Todo excepto patas'),
    ('Bardas de Vaqueta', 810, 'Armadura ligera para caballería', 'Animal', '2', '75', 'Todo excepto patas'),
    ('Conectio', 452, 'Túnica de tela con láminas de metal superpuestas a manera de escamas', 'Metálica', '5', '150', 'Todo excepto cabeza'),
    ('Garro de Cuero', 18, 'Casco fabricado en cuero', 'Casco', '1', '20', 'Cabeza');
''')
# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada y tabla 'Armas' configurada correctamente.")