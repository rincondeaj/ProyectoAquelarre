# Diccionarios precomputados para acceso O(1)
REINOS = {
    1: "Corona de Castilla", 2: "Corona de Castilla",
    3: "Corona de Castilla", 4: "Corona de Castilla",
    5: "Corona de Aragón", 6: "Corona de Aragón",
    7: "Reino de Granada", 8: "Reino de Navarra",
    9: "Reino de Portugal", 10: "Reino de Portugal"
}

# Matriz de culturas para acceso directo O(1)
CULTURAS = {
    "Corona de Castilla": ["Castellano"]*3 + ["Gallego"]*2 + ["Vasco"] + ["Asturicones"],
    "Corona de Aragón": ["Aragonés"]*4 + ["Catalán"]*4 + ["Mudéjar", "Judío"],
    "Reino de Granada": ["Árabe"]*8 + ["Judío", "Mozárabe"],
    "Reino de Navarra": ["Navarro"]*6 + ["Vasco"]*3 + ["Judío"],
    "Reino de Portugal": ["Portugués"]*6 + ["Judío"]*2 + ["Mudéjar"]*2
}

#Diccionario para generar el tipo de posición social
TIPO_POSICION_SOCIAL = {
    'Árabe' : 'Islámico',
    'Aragonés' : 'Cristiano',
    'Asturicones' : 'Cristiano',
    'Castellano' : 'Cristiano',
    'Catalán' : 'Cristiano',
    'Gallego' : 'Cristiano',
    'Judío' : 'Judío',
    'Mozárabe' : 'Islámico',
    'Mudéjar' : 'Cristiano',
    'Navarro' : 'Cristiano',
    'Portugués' : 'Cristiano',
    'Vasco' : 'Cristiano'
}

# Matriz de posición social para acceso directo O(1)
POSICION_SOCIAL_CRISTIANA = {
    1: ("Alta Nobleza", ["Duque/Duquesa", "Marqués/Marquesa", "Conde/Condesa", "Conde/Condesa", 
                       "Vizconde/Vizcondesa", "Vizconde/Vizcondesa", "Vizconde/Vizcondesa",
                       "Barón/Baronesa", "Barón/Baronesa", "Barón/Baronesa"]),
    2: ("Baja Nobleza", ["Señor/Señora", "Señor/Señora", "Caballero/Dama", "Caballero/Dama", 
                       "Caballero/Dama", "Hidalgo", "Hidalgo", "Hidalgo", "Hidalgo", "Hidalgo"]),
    3: ("Burguesía", ["Burgués/Burguesa"]),
    4: ("Burguesía", ["Burgués/Burguesa"]),
    5: ("Villanos", ["Villano/Villana"]),
    6: ("Villanos", ["Villano/Villana"]),
    7: ("Campesinos", ["Colono", "Colono", "Colono", "Vasallo", "Vasallo", "Vasallo", 
                     "Vasallo", "Vasallo", "Vasallo", "Siervo de la Gleba"]),
    8: ("Campesinos", ["Colono", "Colono", "Colono", "Vasallo", "Vasallo", "Vasallo",
                     "Vasallo", "Vasallo", "Vasallo", "Siervo de la Gleba"]),
    9: ("Campesinos", ["Colono", "Colono", "Colono", "Vasallo", "Vasallo", "Vasallo",
                     "Vasallo", "Vasallo", "Vasallo", "Siervo de la Gleba"]),
    10: ("Esclavo", ["Esclavo/Esclava"])
}

# Matriz de posición social para acceso directo O(1)
POSICION_SOCIAL_JUDAICA = {
    1: ("Burguesia", ["Banquero", "Comerciante", "Médico", "Consejero Real"]),
    2: ("Burguesia", ["Banquero", "Comerciante", "Médico", "Consejero Real"]),
    3: ("Burguesia", ["Banquero", "Comerciante", "Médico", "Consejero Real"]),
    4: ("Burguesia", ["Banquero", "Comerciante", "Médico", "Consejero Real"]),
    5: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"]),
    6: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"]),
    7: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"]),
    8: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"]),
    9: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"]),
    10: ("Villanos", ["Artífice", "Sastre", "Orfebre", "Zapatero", "Tejedor"])
}
# Matriz de posición social para acceso directo O(1)
POSICION_SOCIAL_ISLAMICA = {
    1: ("Alta Nobleza", [
        "Sharif (Jerife)",
        "Shaykh (Jeque)", "Shaykh (Jeque)",
        "Emir", "Emir", "Emir",
        "Qadi (Cadí)", "Qadi (Cadí)", "Qadi (Cadí)", "Qadi (Cadí)"
    ]),
    2: ("Baja Nobleza", [
        "Sa'id (Sefón)", "Sa'id (Sefón)", "Sa'id (Sefón)",
        "Al-Barrarze", "Al-Barrarze", "Al-Barrarze",
        "Al-Barrarze", "Al-Barrarze", "Al-Barrarze", "Al-Barrarze"
    ]),
    3: ("Mercaderes", ["Mercader"]),
    4: ("Mercaderes", ["Mercader"]),
    5: ("Ciudadanos", ["Artesano", "Comerciante", "Gremial"]),
    6: ("Ciudadanos", ["Artesano", "Comerciante", "Gremial"]),
    7: ("Ciudadanos", ["Artesano", "Comerciante", "Gremial"]),
    8: ("Campesinos", ["Campesino", "Campesino", "Campesino", "Labrador"]),
    9: ("Campesinos", ["Campesino", "Campesino", "Campesino", "Labrador"]),
    10: ("Esclavo", [
        "Esclavo", "Esclavo", "Esclavo", "Esclavo",
        "Esclavo", "Esclavo", "Esclavo", "Esclavo",
        "Eunuco", "Eunuco"
    ])
}

# Sociedad Cristiana
TRABAJOS_SOCIEDAD_CRISTIANA = {
    "Alta Nobleza": {
        (1, 10): "Alquimista",
        (11, 20): "Caballero de Orden Militar",
        (21, 40): "Clérigo",
        (41, 60): "Cortesano",
        (61, 80): "Infanzón",
        (81, 90): "Monje",
        (91, 100): "Trovador"
    },
    "Baja Nobleza": {
        (1, 10): "Alquimista",
        (11, 20): "Ama",
        (21, 30): "Caballero de Orden Militar",
        (31, 40): "Clérigo",
        (41, 60): "Cortesano",
        (61, 80): "Infanzón",
        (81, 90): "Monje",
        (91, 100): "Trovador"
    },
    "Burguesía": {
        (1, 5): "Alguacil",
        (6, 15): "Alquimista",
        (16, 20): "Barbero Cirujano",
        (21, 30): "Cambista",
        (31, 40): "Comerciante",
        (41, 50): "Escriba",
        (51, 55): "Marino",
        (56, 65): "Médico",
        (66, 70): "Monje",
        (71, 75): "Pardo",
        (76, 80): "Pirata",
        (81, 90): "Sacerdote",
        (91, 100): "Soldado"
    },
    "Campesinos": {
        (1, 5): "Almogávar",
        (6, 15): "Bandido",
        (16, 20): "Brujo",
        (21, 30): "Cazador",
        (31, 40): "Curandero",
        (41, 45): "Mendigo",
        (46, 55): "Monje",
        (56, 60): "Pardo",
        (61, 70): "Pastor",
        (71, 75): "Ramera",
        (76, 80): "Sacerdote",
        (81, 90): "Siervo de Corte",
        (91, 100): "Soldado"
    },
    "Esclavo": {
        (1, 10): "Bufón",
        (11, 20): "Curandero",
        (21, 30): "Escriba",
        (31, 40): "Juglar",
        (41, 50): "Mendigo",
        (51, 60): "Pastor",
        (61, 70): "Ramera",
        (71, 90): "Siervo de Corte",
        (91, 100): "Soldado"
    },
    "Villanos": {
        (1, 10): "Artesano",
        (11, 20): "Barbero Cirujano",
        (21, 25): "Bufón",
        (26, 30): "Cómico",
        (31, 35): "Embaucador",
        (36, 45): "Juglar",
        (46, 55): "Ladrón",
        (56, 60): "Malsín",
        (61, 70): "Marino",
        (71, 75): "Mendigo",
        (76, 85): "Muccadim",
        (86, 90): "Pirata",
        (91, 95): "Ramera",
        (96, 100): "Siervo de Corte"
    }
}

# Sociedad Islámica
TRABAJOS_SOCIEDAD_ISLAMICA = {
    "Alta Nobleza": {
        (1, 10): "Alquimista",
        (11, 30): "Cortesano",
        (31, 40): "Ghazí",
        (41, 60): "Infanzón",
        (61, 70): "Mago",
        (71, 80): "Trovador",
        (81, 100): "Ulema"
    },
    "Baja Nobleza": {
        (1, 10): "Alquimista",
        (11, 30): "Cortesano",
        (31, 40): "Derviche",
        (41, 60): "Ghazí",
        (61, 80): "Infanzón",
        (81, 90): "Mago",
        (91, 100): "Trovador"
    },
    "Mercaderes": {
        (1, 5): "Alguacil",
        (6, 15): "Alquimista",
        (16, 20): "Barbero Cirujano",
        (21, 30): "Cambista",
        (31, 40): "Comerciante",
        (41, 45): "Derviche",
        (46, 55): "Escriba",
        (56, 60): "Ghazí",
        (61, 65): "Mago",
        (66, 70): "Marino",
        (71, 80): "Médico",
        (81, 90): "Rabino"
    },
    "Campesinos": {
        (1, 10): "Bandido",
        (11, 20): "Brujo",
        (21, 30): "Cazador",
        (31, 40): "Curandero",
        (41, 45): "Ghazí",
        (46, 55): "Mendigo",
        (56, 60): "Pardo",
        (61, 70): "Pastor",
        (71, 80): "Ramera",
        (81, 90): "Siervo de Corte",
        (91, 100): "Soldado"
    },
    "Esclavo": {
        (1, 10): "Bufón",
        (11, 20): "Curandero",
        (21, 30): "Escriba",
        (31, 40): "Juglar",
        (41, 50): "Mendigo",
        (51, 60): "Pastor",
        (61, 70): "Qaína",
        (71, 80): "Ramera",
        (81, 90): "Siervo de Corte",
        (91, 100): "Soldado"
    },
    "Ciudadanos": {
        (1, 5): "Alguacil",
        (6, 15): "Artesano",
        (16, 20): "Barbero Cirujano",
        (21, 25): "Bufón",
        (26, 30): "Cómico",
        (31, 35): "Derviche",
        (36, 40): "Embaucador",
        (41, 45): "Ghazí",
        (46, 50): "Juglar",
        (51, 55): "Ladrón",
        (56, 65): "Marino",
        (66, 70): "Mendigo",
        (71, 75): "Pardo",
        (76, 80): "Pirata",
        (81, 85): "Qaína",
        (86, 90): "Ramera",
        (91, 95): "Siervo de Corte",
        (96, 100): "Soldado"
    }
}

# Sociedad Judía
TRABAJOS_SOCIEDAD_JUDIA = {
    "Burguesia": {
        (1, 10): "Alquimista",
        (11, 20): "Barbero Cirujano",
        (21, 30): "Cambista",
        (31, 40): "Comerciante",
        (41, 50): "Escriba",
        (51, 60): "Marino",
        (61, 70): "Médico",
        (71, 80): "Mendigo",
        (81, 90): "Pirata",
        (91, 100): "Rabino"
    },
    'Villanos': {
            (1, 5): 'Alguacil',
            (6, 15): 'Artesano',
            (16, 20): 'Barbero Cirujano',
            (21, 25): 'Bufon',
            (26, 30): 'Comico',
            (31, 35): 'Embaucador',
            (36, 40): 'Juglar',
            (41, 45): 'Ladron',
            (46, 50): 'Marino',
            (51, 55): 'Mendigo',
            (56, 60): 'Monje',
            (61, 65): 'Pirata',
            (66, 70): 'Ramera',
            (71, 80): 'Siervo',
            (81, 100): 'Soldado'
        }
    
}


SITUACIONES_FAMILIARES = {
    1: "Hijo bastardo que desconoce sus padres. No tiene hermanos y fue criado por un tutor.",
    2: "Hijo bastardo reconocido por al menos uno de sus padres. Tiene hermanos pero no derechos de herencia.",
    3: "Nacido en matrimonio, ambos padres vivos.",
    7: "Nacido en matrimonio, ambos padres vivos.",
    8: "Nacido en matrimonio, solo vive la madre y hermanos. Si es primogénito, hereda el título paterno.",
    9: "Nacido en matrimonio, solo vive el padre y hermanos.",
    10: "Nacido en matrimonio, ambos padres fallecidos, solo hermanos. Si es primogénito, hereda el título."
}

TIPOS_BASTARDIA = {
    1: "Fonrecido: Hijo de adulterio, relación incestuosa o de religioso/a.",
    2: "Fonrecido: Hijo de adulterio, relación incestuosa o de religioso/a.",
    3: "Espanto: Hijo de concubina no reconocido por el padre.",
    4: "Espanto: Hijo de concubina no reconocido por el padre.",
    5: "Mansur: Hijo de prostituta.",
    6: "Mansur: Hijo de prostituta.",
    7: "Natural: Hijo de concubina reconocido por el padre.",
    8: "Natural: Hijo de concubina reconocido por el padre.",
    9: "Nato: Hijo de adulterio criado por el marido engañado como propio.",
    10: "Nato: Hijo de adulterio criado por el marido engañado como propio."
}

TIPOS_AREA = [
    "Ciudad",
    "Campo",
    "Montaña",
    "Costa",
    "Desierto",
    "Bosque",
    "Selva",
    "Pueblo",
    "Isla",
    "Valle",
    "Playa",
    "Zona urbana",
    "Zona rural",
    "Suburbio",
    "Altiplano",
    "Llanura",
    "Delta",
    "Estepa",
    "Tundra"
]

COMPETENCIAS_NUEVAS = [
    "Mentoría",
    "Criptografía",
    "Falsificación",
    "Supervivencia",
    "Oratoria",
    "Sabotaje",
    "Contrabando",
    "Heráldica",
    "Cartografía",
    "Intuición",
    "Poética",
    "Cerrajería",
    "Escalada",
    "Camuflaje",
    "Arquitectura",
    "Ceremonial",
    "Encantamiento",
    "Compostura",
    "Cetrería",
    "Sigilografía",
    "Costura",
    "Runología",
    "Videncia",
    "Contorsionismo"
]

TABLA_PESO_ALTURA = {
    5:   {"altura_varas": 1.52, "peso_libras": 106},
    6:   {"altura_varas": 1.54, "peso_libras": 110},
    7:   {"altura_varas": 1.57, "peso_libras": 118},
    8:   {"altura_varas": 1.59, "peso_libras": 120},
    9:   {"altura_varas": 1.62, "peso_libras": 122},
    10:  {"altura_varas": 1.64, "peso_libras": 125},
    11:  {"altura_varas": 1.67, "peso_libras": 128},
    12:  {"altura_varas": 1.69, "peso_libras": 132},
    13:  {"altura_varas": 1.72, "peso_libras": 134},
    14:  {"altura_varas": 1.74, "peso_libras": 140},
    15:  {"altura_varas": 1.77, "peso_libras": 146},
    16:  {"altura_varas": 1.79, "peso_libras": 150},
    17:  {"altura_varas": 1.79, "peso_libras": 150},
    18:  {"altura_varas": 1.79, "peso_libras": 150},
    19:  {"altura_varas": 1.79, "peso_libras": 150},
    20:  {"altura_varas": 1.79, "peso_libras": 150}, # Para 16 o más
}
