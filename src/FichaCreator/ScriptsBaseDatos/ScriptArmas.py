import sqlite3

# Crear o conectar a la base de datos SQLite
conexion = sqlite3.connect("BaseDatos/armas.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Armas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Competencia TEXT NOT NULL,
        Precio INTEGER NOT NULL,
        Descripcion TEXT NOT NULL,
        Dano TEXT NOT NULL,
        Tamano TEXT NOT NULL,
        Recarga TEXT NOT NULL,
        Alcance TEXT NOT NULL,
        Notas TEXT NOT NULL
    );         
''')
# Crear la tabla Armas
cursor.execute('''
INSERT INTO Armas (Nombre, Competencia, Precio, Descripcion, Dano, Tamano, Recarga, Alcance, Notas) VALUES
('Alfanje', 'Espadones', '108', 'Hoja ancha, ligeramente curvada y de un solo filo', '1d10 +1', 'Pes', 'NA', '-', 'Requiere dos manos'),
('Almarada', 'Cuchillos', '3', 'Cuchillos con filo de acero y empuñadura de madera', '1d4 +2', 'Lig', 'NA', '-', 'Arma básica'),
('Arbalesta', 'Ballestas', '216', 'Ballestas pesada que requiere cranequín para recargar', '1d10 +2', 'Pes', '5 turnos', '80/320', 'Daño penetrante'),
('Archa', 'Hachas', '36', 'Mezcla de hacha y lanza (1.5-2 varas)', '1d10 +1', 'Pes', 'NA', '-', 'Versátil'),
('Arco Corto', 'Arcos', '36', 'Arco de tamaño Med para cazadores', '1d6', 'Med', '1 turno', '40/60', 'Munición incluida'),
('Arco Largo', 'Arcos', '108', 'Extremadamente raro en reinos peninsulares', '1d10', 'Pes', '1 turno', '100/400', 'Elite'),
('Arco Recurvado', 'Arcos', '72', 'Utilizado en el reino de Granada', '1d10', 'Med', '1 turno', '90/360', 'Precisión'),
('Ballesta', 'Ballestas', '136', 'Madera con palas metálicas', '1d10', 'Med', '3 turnos', '60/240', 'Estándar'),
('Ballesta Ligera', 'Ballestas', '108', 'Versión reducida para cacerías nobles', '1d6', 'Med', '2 turnos', '50/200', 'Noble'),
('Bastón de Combate', 'Bastónes', '2', 'Bastón de madera de una vara', '1d4', 'Med', 'NA', '-', 'Improvisada'),
('Bordam', 'Bastónes', '3', 'Palo de 1.7-2 varas para caminantes', '1d4 +2', 'Med', 'NA', '-', 'Apoyo'),
('Bracamante', 'Cuchillos', '68', 'Usada por cazadores y marineros', '1d6'+2, 'Lig', 'NA', '-', 'Despiece'),
('Cayado', 'Bastónes', '3', 'Vara gruesa de pastores', '1d4 +1', 'Med', 'NA', '-', 'Rústico'),
('Clava', 'Garrotes', '2', 'Garrote de madera simple', '1d6', 'Med', 'NA', '-', 'Primitiva'),
('Colell', 'Cuchillos', '10', 'Cuchillos de almogávar', '1d6 +1', 'Lig', 'NA', '-', 'Militar'),
('Cuchillos', 'Cuchillos', '3', 'Herramienta/arma improvisada', '1d6', 'Lig', 'NA', '-', 'Básico'),
('Dubus', 'Mazas', '6', 'Maza con refuerzos metálicos', '1d6 +1', 'Med', 'NA', '-', 'Contundente'),
('Daga', 'Dagas', '12', 'Arma secundaria de la nobleza', '2d3', 'Lig', 'NA', '-', 'Elegante'),
('Espada Bastarda', 'Espadas', '85', 'Empuñadura para una o dos manos', '1d10', 'Pes', 'NA', '-', 'Versátil'),
('Espada Coria', 'Espadas', '51', 'Hoja de doble filo (media vara)', '1d8 +1', 'Med', 'NA', '-', 'Equilibrada'),
('Espada de Mano', 'Espadas', '68', 'Hoja recta de doble filo (1 vara)', '1d8 +1', 'Med', 'NA', '-', 'Estándar'),
('Estilete', 'Dagas', '12', 'Daga pequeña punzante', '1d3 +1', 'Lig', 'NA', '-', 'Perforante'),
('Estoque', 'Espadas', '51', 'Espada de filo estrecho', '1d8', 'Med', 'NA', '-', 'Precisión'),
('Gumia', 'Dagas', '12', 'Daga marroquí de hoja curva', '1d4 +2', 'Lig', 'NA', '-', 'Exótica'),
('Hacha', 'Hachas', '2', 'Herramienta/arma improvisada', '1d6', 'Med', 'NA', '-', 'Versátil'),
('Hacha de Armas', 'Hachas', '6', 'Diseñada para guerra, totalmente metálica', '1d8 +2', 'Med', 'NA', '-', 'Militar'),
('Hacha de Combate', 'Hachas', '27', 'Filo doble, requiere dos manos', '1d10 + 1d4', 'Pes', 'NA', '-', 'Poderosa'),
('Hacha de Petos', 'Hachas', '36', 'Hacha especial para combate', '1D10', 'Pes', 'NA', '-', 'Requiere Fuerza 12'),
('Honda', 'Hondas', '1', 'Arma de proyectiles simples', '1D3+2', 'Lig', '1', '15/25/50', 'Usa Percepción'),
('Horquilla', 'Lanzas', '36', 'Lanza con punta bifurcada', '1D8', 'Med', 'NA', '-', 'Requiere Agilidad'),
('Jineta Nasiri', 'Espadas', '360', 'Espada árabe curva', '1D6+2', 'Med', 'NA', '-', 'Usa Habilidad'),
('Lanza Corta', 'Lanzas', '6', 'Lanza versátil para infantería', '1D6+1', 'Med', 'NA', '-', 'Requiere FUE'),
('Lanza de Caballería', 'Lanzas', '10', 'Lanza especial para carga montada', '2D6', 'Pes', 'NA', '-', 'Daño potente'),
('Lanza Larga', 'Lanzas', '12', 'Lanza de gran alcance', '1D8+2', 'Pes', 'NA', '-', 'Para formación'),
('Mangual', 'Mazas', '216', 'Arma de cadena con peso', '1D8', 'Med', 'NA', '-', 'Requiere Fuerza'),
('Martillo de Guerra', 'Mazas', '51', 'Martillo de combate Pes', '1D8+1', 'Med', 'NA', '-', 'Contundente'),
('Mayal de Armas', 'Mazas', '72', 'Versión bélica del mayal', '1D10', 'Pes', 'NA', '-', 'Impacto devastador'),
('Maza', 'Mazas', '7', 'Arma contundente básica', '1D8', 'Med', 'NA', '-', 'Estándar'),
('Maza de Armas', 'Mazas', '10', 'Maza reforzada para combate', '1D8+2', 'Med', 'NA', '-', 'Mejor balance'),
('Maza Pesada', 'Mazas', '14', 'Maza de gran tamaño', '2D6', 'Pes', 'NA', '-', 'Requiere Fuerza 15'),
('Montante', 'Espadones', '108', 'Espada enorme a dos manos', '1D10+2', 'Pes', 'NA', '-', 'Para expertos'),
('Morosa', 'Lanzas', '18', 'Lanza pesada especial', '2D6', 'Pes', 'NA', '-', 'Elite'),
('Nimcia', 'Espadas', '68', 'Espada equilibrada', '1D6+2', 'Med', 'NA', '-', 'Precisión'),
('Pico de Cuervo', 'Hachas', '72', 'Hacha con punta aguda', '1D8+1', 'Med', 'NA', '-', 'Versátil'),
('Saif', 'Espadas', '68', 'Espada curva árabe', '1D6+2', 'Med', 'NA', '-', 'Corte rápido'),
('Takuba', 'Espadas', '68', 'Espada africana', '1D8+1', 'Med', 'NA', '-', 'Balanceada'),
('Telek', 'Cuchillos', '14', 'Cuchillo Ligero', '1D3+2', 'Lig', 'NA', '-', 'Preciso'),
('Terciado', 'Cuchillos', '18', 'Cuchillo de combate', '1D6+1', 'Lig', 'NA', '-', 'Afiliado'),
('Tripa', 'Mazas', '2', 'Maza ligera', '1D4+2', 'Lig', 'NA', '-', 'Rápida');
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada y tabla 'Armas' configurada correctamente.")