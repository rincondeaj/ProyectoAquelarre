import random
import string
import sqlite3
from data import REINOS, CULTURAS, POSICION_SOCIAL_CRISTIANA, TIPO_POSICION_SOCIAL, POSICION_SOCIAL_JUDAICA, POSICION_SOCIAL_ISLAMICA
from data import TRABAJOS_SOCIEDAD_CRISTIANA, TRABAJOS_SOCIEDAD_ISLAMICA, TRABAJOS_SOCIEDAD_JUDIA
from nombres import NOMBRES_ARAGONESES, NOMBRES_CASTELLANOS, NOMBRES_CATALANES, NOMBRES_EUSKERAS, NOMBRES_GALLEGO_PORTUGUESES, NOMBRES_HEBREOS, NOMBRES_MUSULMANES
from data import SITUACIONES_FAMILIARES, TIPOS_BASTARDIA, TIPOS_AREA, COMPETENCIAS_NUEVAS, TABLA_PESO_ALTURA
import os

#Variable global
TOTAL_CARACTERISTICAS = 0

class GeneradorPersonaje:
    __slots__ = [
        '_reino', '_etnia', '_sexo', '_tipo', '_categoria', '_titulo', '_profesion',
        '_profesionPaterna', '_situacionFamiliar', '_situacionClave', '_fuerza', '_agilidad',
        '_habilidad', '_resistencia', '_percepcion', '_comunicacion', '_cultura', '_aspecto',
        '_suerte', 'idiomas_seleccionados', 'areas_seleccionadas', 'auxiliares_seleccionadas',
        '_irracionalidad', '_racionalidad', '_dinero', '_gasto'
    ]  # Optimización de memoria

    def __init__(self):
        self._reino = None
        self._etnia = None
        self.idiomas_seleccionados = set()  # Mantener un registro de los idiomas ya seleccionados
        self.areas_seleccionadas = set()  # Mantener un registro de las áreas ya seleccionadas
        self.auxiliares_seleccionadas = set()  # Mantener un registro de las competencias auxiliares seleccionadas
    
    @property
    def reino(self):
        if self._reino is None:
            self._reino = REINOS[random.randint(1, 10)]
        return self._reino
    
    def nombre(self, sexo, etnia, valor=None):
        self._sexo = sexo
        if valor is not None:
            return f"{valor}    ({sexo})"  # Si se proporciona un valor, devolverlo directamente
        if etnia in ['Portugués', 'Gallego']:
            nombre = random.choice(NOMBRES_GALLEGO_PORTUGUESES[sexo])
        elif etnia in ['Vasco', 'Asturicones', 'Navarro']:
            nombre = random.choice(NOMBRES_EUSKERAS[sexo])
        elif etnia == 'Castellano':
            nombre = random.choice(NOMBRES_CASTELLANOS[sexo])
        elif etnia == 'Aragonés':
            nombre = random.choice(NOMBRES_ARAGONESES[sexo])
        elif etnia == 'Catalán':
            nombre = random.choice(NOMBRES_CATALANES[sexo])
        elif etnia in ['Mudéjar', 'Árabe']:
            nombre = random.choice(NOMBRES_MUSULMANES[sexo])
        elif etnia in ['Mozárabe', 'Judío']:
            nombre = random.choice(NOMBRES_HEBREOS[sexo])
        else:
            nombre = "Desconocido"
        
        return f"{nombre}   ({sexo})"
    
    def etnia(self, valor=None):
        if valor is not None:
            return valor  # Si se proporciona un valor, devolverlo directamente
        if self._etnia is None:
            culturas_reino = CULTURAS[self.reino]
            self._etnia = culturas_reino[random.randint(0, len(culturas_reino) - 1)]
        return self._etnia
    
    def posicion_social(self, etnia, valor=None):
        if valor is not None:
            return f"{etnia} -> {valor}"  # Si se proporciona un valor, devolverlo directamente
        self._tipo = TIPO_POSICION_SOCIAL[etnia]
        
        if self._tipo == 'Cristiano':
            clave = random.randint(1, 10)
            self._categoria, opciones = POSICION_SOCIAL_CRISTIANA[clave]
            self._titulo = random.choice(opciones)
            return f"{self._categoria} -> {self._titulo}"
        
        elif self._tipo == 'Islámico':
            clave = random.randint(1, 10)
            self._categoria, opciones = POSICION_SOCIAL_ISLAMICA[clave]
            self._titulo = random.choice(opciones)
            return f"{self._categoria} -> {self._titulo}"
            
        elif self._tipo == 'Judío':
            clave = random.randint(1, 10)
            self._categoria, opciones = POSICION_SOCIAL_JUDAICA[clave]
            self._titulo = random.choice(opciones)
            return f"{self._categoria} -> {self._titulo}"
        
        return "Desconocido"
    
    def profesion(self, tipo, categoria, valor=None):
        if valor is not None:
            return valor  # Si se proporciona un valor, devolverlo directamente
        try:
            if tipo == 'Cristiano':
                rangos_profesion = TRABAJOS_SOCIEDAD_CRISTIANA[categoria]
            elif tipo == 'Islámico':
                rangos_profesion = TRABAJOS_SOCIEDAD_ISLAMICA[categoria]
            elif tipo == 'Judío':
                rangos_profesion = TRABAJOS_SOCIEDAD_JUDIA[categoria]
            else:
                return "Vago"
            
            tirada = random.randint(1, 100)
            
            for rango, profesion in rangos_profesion.items():
                if rango[0] <= tirada <= rango[1]:
                    self._profesion = profesion
                    if(self.profesion == "Ramera"):
                        print("Si")
                    return self._profesion
            
            return "Profesión no encontrada"
        
    
        except KeyError as e:
            print(f"Error al buscar profesión: {e}")
            print(f"Datos usados - Tipo: {tipo}, Categoría: {categoria}")
            return "Error en profesión"
        
    def jugador(self):
        return "NPC"
    
    def profesionPaterna(self, valor=None):
        if valor is not None:
            return valor  # Si se proporciona un valor, devolverlo directamente

        # Elegir aleatoriamente una de las sociedades
        opcion = random.choice([TRABAJOS_SOCIEDAD_CRISTIANA, TRABAJOS_SOCIEDAD_ISLAMICA, TRABAJOS_SOCIEDAD_JUDIA])

        # Elegir una categoría aleatoria dentro de la sociedad seleccionada
        categoria = random.choice(list(opcion.keys()))

        # Elegir un trabajo aleatorio dentro de la categoría seleccionada
        tirada = random.randint(1, 100)
        for rango, profesion in opcion[categoria].items():
            if rango[0] <= tirada <= rango[1]:
                return profesion

        return "Profesión paterna no encontrada"
    
    def situacionFamiliar(self):
        # Verificar si ya se ha generado una situación familiar
        if not hasattr(self, '_situacionFamiliar'):
            # Elegir una situación familiar al azar
            situacion = random.choice(list(SITUACIONES_FAMILIARES.keys()))
            # Guardar la clave de la situación
            self._situacionClave = situacion
            # Obtener el texto asociado a la situación
            texto = SITUACIONES_FAMILIARES[situacion]
            # Guardar la situación seleccionada en un atributo
            self._situacionFamiliar = texto
        else:
            # Recuperar la clave de la situación ya generada
            situacion = self._situacionClave
            texto = self._situacionFamiliar

        # Si es bastardo (situaciones 1 o 2), añadir el tipo de bastardía
        if situacion in [1, 2]:
            texto += f"   Tipo de bastardía: {random.choice(list(TIPOS_BASTARDIA.values()))}"

        # Dividir el texto en partes de máximo 70 caracteres
        partes = [texto[i:i+70] for i in range(0, len(texto), 70)]

        # Asegurarse de que haya exactamente 4 partes
        while len(partes) < 4:
            partes.append("")  # Rellenar con cadenas vacías si hay menos de 4 partes

        # Retornar las partes como un diccionario
        return {
            "Descripcion1": partes[0],
            "Descripcion2": partes[1],
            "Descripcion3": partes[2],
            "Descripcion4": partes[3]
        }

    def familia(self):
        return "(En descripción)"
    
    def gen_caracteristicas(self, trabajo, campo, calidad = None, belleza = None):
        """
        Genera las características del personaje basándose en el trabajo seleccionado
        y el campo específico solicitado. Ajusta las características si es necesario.
        """
        global TOTAL_CARACTERISTICAS  # Usar la variable global

        # Ruta absoluta de la base de datos
        db_path = os.path.join(os.getcwd(), "BaseDatos/profesiones.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            print(f"Error: No se encontró la base de datos en {db_path}")
            return None

        try:

            conexion = sqlite3.connect(db_path)
            cursor = conexion.cursor()

            # Construir la consulta SQL con el campo dinámico
            query = f"SELECT {campo} FROM Profesiones WHERE Nombre = ?"
            cursor.execute(query, (trabajo,))
            resultado = cursor.fetchone()

            if resultado:
                valor = resultado[0]

                # Asignar el valor a la característica correspondiente y ajustar si es necesario
                if campo == "Fuerza":
                    self._fuerza = valor
                    self._fuerza = self._ajustar_valor(self._fuerza, calidad)
                elif campo == "Agilidad":
                    self._agilidad = valor
                    self._agilidad = self._ajustar_valor(self._agilidad, calidad)
                elif campo == "Habilidad":
                    self._habilidad = valor
                    self._habilidad = self._ajustar_valor(self._habilidad, calidad)
                elif campo == "Resistencia":
                    self._resistencia = valor
                    self._resistencia = self._ajustar_valor(self._resistencia, calidad)
                elif campo == "Percepcion":
                    self._percepcion = valor
                    self._percepcion = self._ajustar_valor(self._percepcion, calidad)
                elif campo == "Comunicacion":
                    self._comunicacion = valor
                    self._comunicacion = self._ajustar_valor(self._comunicacion, calidad)
                elif campo == "Cultura":
                    self._cultura = valor
                    self._cultura = self._ajustar_valor(self._cultura, calidad)
                elif campo == "Aspecto":
                    self._aspecto = valor
                    self._aspecto = self.ajustarAspecto(self._aspecto, belleza)
                elif campo == "Suerte":
                    self._suerte = valor + random.randint(1, 40)

                # Sumar el valor al total si es una de las características principales
                if campo in ["Fuerza", "Agilidad", "Habilidad", "Resistencia", "Percepcion", "Comunicacion", "Cultura"]:
                    TOTAL_CARACTERISTICAS += valor

                if campo == "Fuerza":
                    return self._fuerza
                elif campo == "Agilidad":
                    return self._agilidad
                elif campo == "Habilidad":
                    return self._habilidad
                elif campo == "Resistencia":
                    return self._resistencia
                elif campo == "Percepcion":
                    return self._percepcion
                elif campo == "Comunicacion":
                    return self._comunicacion
                elif campo == "Cultura":
                    return self._cultura
                elif campo == "Aspecto":
                    return self._aspecto
                elif campo == "Suerte":
                    return self._suerte

            else:
                print(f"Trabajo '{trabajo}' no encontrado en la base de datos.")
                return None

        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
            return None

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def _ajustar_valor(self, valor_actual, calidad = None):
        """
        Ajusta el valor de una característica si TOTAL_CARACTERISTICAS <= 100
        y el valor actual es menor que 20.
        """
        global TOTAL_CARACTERISTICAS
        if calidad:
            if(calidad == "Malo"):
                opcion = 5
            elif(calidad == "Neutral"):
                opcion = 10
            elif(calidad == "Bueno"):
                opcion = 15
            
        opcion = random.randint(5,15)

        if TOTAL_CARACTERISTICAS <= 100 and valor_actual < 20:
            incremento = random.randint(1, min(opcion, 20 - valor_actual))  # Incremento aleatorio entre 1 y el límite permitido
            TOTAL_CARACTERISTICAS += incremento
            return valor_actual + incremento

        return valor_actual

    def ajustarAspecto(self, valor_actual, belleza):
        number = 0
        if(self._sexo == 'mujer'):
            number += 2
        for i in range(4):
            number += random.randint(1,6)
        if valor_actual == 17 and number < 17 and self._sexo == 'mujer':
            return valor_actual + 2
        return number

    def getArea(self):
        """
        Selecciona un área aleatoria de TIPOS_AREA, asegurándose de no repetir áreas ya seleccionadas.
        """
        # Filtrar las áreas disponibles que aún no han sido seleccionadas
        areas_disponibles = [area for area in TIPOS_AREA if area not in self.areas_seleccionadas]

        if areas_disponibles:
            # Seleccionar un área aleatoria de las disponibles
            area = random.choice(areas_disponibles)
            self.areas_seleccionadas.add(area)  # Marcar el área como seleccionada
            return area
        else:
            print("No hay más áreas disponibles para seleccionar.")
            return "Sin áreas disponibles"
       
    def getIdioma(self, profesion):
        """
        Selecciona un idioma con el que la profesión sea competente, basado en el tipo 'Idiomas',
        asegurándose de no seleccionar el mismo idioma dos veces.
        """

        # Ruta absoluta de la base de datos
        db_path = os.path.join(os.getcwd(), "BaseDatos/profesiones.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            print(f"Error: No se encontró la base de datos en {db_path}")
            return None
        
        # Conectar a la base de datos
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()

        try:
            # Construir la consulta SQL para buscar competencias de tipo 'Idiomas' asociadas a la profesión
            query = """
            SELECT Competencias.Nombre
            FROM Profesion_Competencia, Competencias, Profesiones
            WHERE Profesiones.id = Profesion_Competencia.profesion_id
            AND Competencias.id = Profesion_Competencia.competencia_id
            AND Profesiones.Nombre = ?
            AND Profesion_Competencia.tipo = 'Idiomas'
            """
            cursor.execute(query, (profesion,))
            resultado = cursor.fetchall()

            if resultado:
                # Filtrar los idiomas que aún no han sido seleccionados
                idiomas_disponibles = [idioma[0] for idioma in resultado if idioma[0] not in self.idiomas_seleccionados]

                if idiomas_disponibles:
                    # Seleccionar un idioma aleatorio de los disponibles
                    idioma = random.choice(idiomas_disponibles)
                    self.idiomas_seleccionados.add(idioma)  # Marcar el idioma como seleccionado
                    return idioma
                else:
                    print(f"Todos los idiomas asociados a la profesión '{profesion}' ya han sido seleccionados.")
                    return "Idioma desconocido"
            else:
                print(f"No se encontraron idiomas asociados a la profesión '{profesion}'.")
                return "Idioma desconocido"

        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
            return "Error en idioma"

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def getCompetenciaAux(self):
        """
        Selecciona una competencia auxiliar aleatoria de TIPOS_COMPETENCIA_AUX,
        asegurándose de no repetir competencias ya seleccionadas.
        """
        # Filtrar las competencias auxiliares disponibles que aún no han sido seleccionadas
        auxiliares_disponibles = [aux for aux in COMPETENCIAS_NUEVAS if aux not in self.auxiliares_seleccionadas]

        if auxiliares_disponibles:
            # Seleccionar una competencia auxiliar aleatoria de las disponibles
            competencia_aux = random.choice(auxiliares_disponibles)
            self.auxiliares_seleccionadas.add(competencia_aux)  # Marcar la competencia como seleccionada
            return competencia_aux
        else:
            print("No hay más competencias auxiliares disponibles para seleccionar.")
            return "Sin competencias auxiliares disponibles"
        
    def genCompetencia(self, profesion, competencia):
        """
        Busca en la tabla Profesion_Competencia la relación entre la profesión y la competencia,
        y devuelve las columnas Caracteristica y tipo. Si no se encuentra, genera un valor aleatorio basado en la característica.
        """

        # Ruta absoluta de la base de datos
        db_path = os.path.join(os.getcwd(), "BaseDatos/profesiones.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            print(f"Error: No se encontró la base de datos en {db_path}")
            return None


        # Conectar a la base de datos
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()

        try:
            # Construir la consulta SQL
            query = """
            SELECT Competencias.Caracteristica, Profesion_Competencia.tipo
            FROM Profesion_Competencia, Profesiones, Competencias
            WHERE Profesion_Competencia.profesion_id = Profesiones.id
            AND Profesion_Competencia.competencia_id = Competencias.id
            AND Profesiones.Nombre = ?
            AND Competencias.Nombre = ?
            """
            cursor.execute(query, (profesion, competencia))
            resultado = cursor.fetchone()
            if resultado:
                print(f"Es competente con {competencia}")
                competencia, tipo = resultado
                if(tipo == 'Primaria'):
                    bonificador = 25
                elif(tipo == 'Secundaria'):
                    bonificador = 10
                else:
                    bonificador = random.randint(1,15)

                if competencia == "Fuerza" or (competencia == "Fuerza" and tipo == "Armas"):
                    return random.randint(self._fuerza, self._fuerza * 5) + bonificador
                elif competencia == "Agilidad" or (competencia == "Agilidad" and tipo == "Armas"):
                    return random.randint(self._agilidad, self._agilidad * 5) +bonificador
                elif competencia == "Habilidad" or (competencia == "Habilidad" and tipo == "Armas"):
                    return random.randint(self._habilidad, self._habilidad * 5) +bonificador
                elif competencia == "Resistencia" or (competencia == "Resistencia" and tipo == "Armas"):
                    return random.randint(self._resistencia, self._resistencia * 5) +bonificador
                elif competencia == "Percepcion" or (competencia == "Percepcion" and tipo == "Armas"):
                    return random.randint(self._percepcion, self._percepcion * 5) +bonificador
                elif competencia == "Comunicacion":
                    return random.randint(self._comunicacion, self._comunicacion * 5) +bonificador
                elif competencia == "Cultura":
                    return random.randint(self._cultura, self._cultura * 5) +bonificador
                elif competencia == "Aspecto":
                    return self._aspecto * 5
                else:
                    print(f"Competencia '{competencia}' no tiene una característica asociada.")
                    return None
            else:
                # Si no se encuentra, generar un valor aleatorio basado en la característica
                query_caracteristica = """
                SELECT Caracteristica
                FROM Competencias
                WHERE Nombre = ?
                """
                cursor.execute(query_caracteristica, (competencia,))
                resultado_caracteristica = cursor.fetchone()
                if resultado_caracteristica:
                    competencia = resultado_caracteristica[0]
                if competencia == "Fuerza":
                    return random.randint(self._fuerza, self._fuerza * 3)
                elif competencia == "Agilidad":
                    return random.randint(self._agilidad, self._agilidad * 3)
                elif competencia == "Habilidad":
                    return random.randint(self._habilidad, self._habilidad * 3)
                elif competencia == "Resistencia":
                    return random.randint(self._resistencia, self._resistencia * 3)
                elif competencia == "Percepcion":
                    return random.randint(self._percepcion, self._percepcion * 3)
                elif competencia == "Comunicacion":
                    return random.randint(self._comunicacion, self._comunicacion * 3)
                elif competencia == "Cultura":
                    return random.randint(self._cultura, self._cultura * 3)
                elif competencia == "Aspecto":
                    return self._aspecto * 5
                else:
                    print(f"Competencia '{competencia}' no tiene una característica asociada.")
                    return None

        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
            return None

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def getAlturaPeso(self):
        alturaPeso = TABLA_PESO_ALTURA[self._resistencia]
        return f"{alturaPeso['altura_varas']} v {alturaPeso['peso_libras']} l"
    
    def getSuerte(self):
        suerteAux = self._comunicacion + self._percepcion + self._cultura
        if(suerteAux > self._suerte):
            self._suerte = suerteAux
        return self._suerte

    def getIrracionalidad(self):
        self._irracionalidad = random.randint(1,100)
        return self._irracionalidad
    
    def getRacionalidad(self):
        self._racionalidad = 100 - self._irracionalidad
        return self._racionalidad

    def getIngresoMensual(self):
        if(self._categoria == 'Alta nobleza'):
            self._dinero = random.randint(1000, 3000)
        elif(self._categoria == 'Baja nobleza'):
            self._dinero =  random.randint(250, 750)
        elif(self._categoria == 'Burguesía' or 'Mercader'):
            self._dinero = random.randint(500, 1000)
        elif(self._categoria == 'Villano' or 'Ciudadano'):
            self._dinero = random.randint(40, 120)
        elif(self._categoria == 'Campesino'):
            self._dinero =  random.randint(20, 60)
        else:
            print("El sueldo es random")
            self._dinero = random.randint(1, 1000)
        return self._dinero
    
    def getDinero(self):
        return self._dinero
    
    def getGasto(self):
        if(self._categoria == 'Alta nobleza'):
            self._gasto = random.randint(250, 500)
        elif(self._categoria == 'Baja nobleza'):
            self._gasto =  random.randint(50, 150)
        elif(self._categoria == 'Burguesía' or 'Mercader'):
            self._gasto = random.randint(100, 300)
        elif(self._categoria == 'Villano' or 'Ciudadano'):
            self._gasto = random.randint(5, 30)
        elif(self._categoria == 'Campesino'):
            self._gasto =  random.randint(3, 20)
        else:
            print("El gasto es random")
            self._gasto = random.randint(1, 200)
        return self._gasto
        
    def getArma(self, slot):
        """
        Obtiene los datos de un arma desde la base de datos para el slot especificado.
        """

        # Ruta absoluta de la base de datos
        db_path = os.path.join(os.getcwd(), "BaseDatos/armas.db")

        # Verificar si la base de datos existe
        if not os.path.exists(db_path):
            print(f"Error: No se encontró la base de datos en {db_path}")
            return None

        # Conectar a la base de datos
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()

        try:
            # Consulta para obtener un arma aleatoria
            query = "SELECT Nombre, Dano, Tamano, Recarga, Alcance, Notas, Competencia FROM Armas ORDER BY RANDOM() LIMIT 1"
            cursor.execute(query)
            resultado = cursor.fetchone()

            if resultado:
                # Retornar los datos del arma como un diccionario con todos los campos necesarios
                return {
                    f"ArmaNombreSlot{slot}": f"{resultado[0]} ({resultado[6]})",
                    f"ArmaPorcentajeSlot{slot}": "100",
                    f"ArmaDanoSlot{slot}": resultado[1],
                    f"ArmaTamanoSlot{slot}": resultado[2],
                    f"ArmaRecargaSlot{slot}": resultado[3],
                    f"ArmaAlcanceSlot{slot}": resultado[4],
                    f"ArmaNotasSlot{slot}": resultado[5],
                }
            else:
                print(f"No se encontraron armas en la base de datos para el slot {slot}.")
                # Retornar un diccionario vacío con los campos del slot para evitar errores
                return {
                    f"ArmaNombreSlot{slot}": "",
                    f"ArmaPorcentajeSlot{slot}": "",
                    f"ArmaDanoSlot{slot}": "",
                    f"ArmaTamanoSlot{slot}": "",
                    f"ArmaRecargaSlot{slot}": "",
                    f"ArmaAlcanceSlot{slot}": "",
                    f"ArmaNotasSlot{slot}": "",
                }

        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos de armas: {e}")
            # Retornar un diccionario vacío con los campos del slot para evitar errores
            return {
                f"ArmaNombreSlot{slot}": "",
                f"ArmaPorcentajeSlot{slot}": "",
                f"ArmaDanoSlot{slot}": "",
                f"ArmaTamanoSlot{slot}": "",
                f"ArmaRecargaSlot{slot}": "",
                f"ArmaAlcanceSlot{slot}": "",
                f"ArmaNotasSlot{slot}": "",
            }

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def generar_valor(self, campo, reino=None, profesion=None):
        # Dispatch table para acceso O(1)
        handlers = {
            'Nombre': lambda: self.nombre(random.choice(['mujer', 'hombre']), self.etnia()),
            'Reino': lambda: reino if reino is not None else self.reino,
            'GrupoEtnico': lambda: self.etnia(),
            'PosicionSocial': lambda: self.posicion_social(self.etnia()),
            'Profesion': lambda: self.profesion(self._tipo, self._categoria, profesion),
            'Sano': lambda: 'Yes_vwih',
            'Jugador': lambda: self.jugador(),
            'ProfesionPaterna': lambda: self.profesionPaterna(),
            'Familia': lambda: self.familia(),
            'CaracteristicasPrincipales': lambda: self.gen_caracteristicas(self._profesion),  # Usar el valor de la profesión
            "Fuerza": lambda: self.gen_caracteristicas(self._profesion, "Fuerza"),
            "Agilidad": lambda: self.gen_caracteristicas(self._profesion, "Agilidad"),
            "Habilidad": lambda: self.gen_caracteristicas(self._profesion, "Habilidad"),
            "Resistencia": lambda: self.gen_caracteristicas(self._profesion, "Resistencia"),
            "Percepcion": lambda: self.gen_caracteristicas(self._profesion, "Percepcion"),
            "Comunicacion": lambda: self.gen_caracteristicas(self._profesion, "Comunicacion"),
            "Cultura": lambda: self.gen_caracteristicas(self._profesion, "Cultura"),
            "Aspecto": lambda: self.gen_caracteristicas(self._profesion, "Aspecto"),
            "Suerte": lambda: self.gen_caracteristicas(self._profesion, "Suerte"),
            "PV": lambda: self._resistencia if self._resistencia is not None else 0,
            "PV_A":  lambda: self._resistencia if self._resistencia is not None else 0,
            "FuerzaTemporal": lambda: self._fuerza if self._fuerza is not None else 0,
            "AgilidadTemporal": lambda: self._agilidad if self._fuerza is not None else 0,
            "HabilidadTemporal": lambda: self._habilidad if self._fuerza is not None else 0,
            "ResistenciaTemporal": lambda: self._resistencia if self._fuerza is not None else 0,
            "PercepcionTemporal": lambda: self._percepcion if self._fuerza is not None else 0,
            "ComunicacionTemporal": lambda: self._comunicacion if self._fuerza is not None else 0,
            "CulturaTemporal": lambda: self._cultura if self._fuerza is not None else 0,
            "AspectoTemporal": lambda: self._aspecto if self._fuerza is not None else 0,
            "Alquimia": lambda: self.genCompetencia(self._profesion, "Alquimia"),
            "Edad": lambda: random.randint(16,40),
            "AlturaPeso": lambda: self.getAlturaPeso(),
            "IRR": lambda: self.getIrracionalidad(),
            "RR": lambda: self.getRacionalidad(),
            "PF": lambda: random.randint(1, 10),
            "PC": lambda: random.randint(1, 10),
            "SuerteActual": lambda: self._suerte if self._suerte is not None else 0,
            "PA": lambda: random.randint(1,100),
            "Artesania": lambda: self.genCompetencia(self._profesion, "Artesania"),
            'Astrologia': lambda: self.genCompetencia(self._profesion, "Astrologia"),
            'Cabalgar': lambda: self.genCompetencia(self._profesion, "Cabalgar"),
            'Cantar': lambda: self.genCompetencia(self._profesion, "Cantar"),
            'Comerciar': lambda: self.genCompetencia(self._profesion, "Comerciar"),
            'ConducirCarro': lambda: self.genCompetencia(self._profesion, "ConducirCarro"),
            'ConAnimal': lambda: self.genCompetencia(self._profesion, "ConAnimal"),
            'ConMagico': lambda: self.genCompetencia(self._profesion, "ConMagico"),
            'ConMineral': lambda: self.genCompetencia(self._profesion, "ConMineral"),
            'ConVegetal': lambda: self.genCompetencia(self._profesion, "ConVegetal"),
            "ConAreaNumSlot1": lambda: self.genCompetencia(self._profesion, "ConAreaNumSlot1"),
            "ConAreaNumSlot2": lambda: self.genCompetencia(self._profesion, "ConAreaNumSlot2"),
            "ConAreaSlot1": lambda: self.getArea(),
            "ConAreaSlot2": lambda: self.getArea(),
            'Correr': lambda: self.genCompetencia(self._profesion, "Correr"),
            'Corte': lambda: self.genCompetencia(self._profesion, "Corte"),
            'Degustar': lambda: self.genCompetencia(self._profesion, "Degustar"),
            'Descubrir': lambda: self.genCompetencia(self._profesion, "Descubrir"),
            'Disfrazarse': lambda: self.genCompetencia(self._profesion, "Disfrazarse"),
            'Elocuencia': lambda: self.genCompetencia(self._profesion, "Elocuencia"),
            'Empatia': lambda: self.genCompetencia(self._profesion, "Empatia"),
            'Ensenar': lambda: self.genCompetencia(self._profesion, "Ensenar"),
            'Escamotear': lambda: self.genCompetencia(self._profesion, "Escamotear"),
            'Escuchar': lambda: self.genCompetencia(self._profesion, "Escuchar"),
            'Esquivar': lambda: self.genCompetencia(self._profesion, "Esquivar"),
            'ForzarMecanismos': lambda: self.genCompetencia(self._profesion, "ForzarMecanismos"),
            'IdiomaSlot1': lambda: self.getIdioma(self._profesion),
            'IdiomaSlot2': lambda: self.getIdioma(self._profesion),
            'IdiomaSlot3': lambda: self.getIdioma(self._profesion),
            'IdiomaNumSlot1': lambda: self.genCompetencia(self._profesion, "IdiomaNumSlot1"),
            'IdiomaNumSlot2': lambda: self.genCompetencia(self._profesion, "IdiomaNumSlot2"),
            'IdiomaNumSlot3': lambda: self.genCompetencia(self._profesion, "IdiomaNumSlot3"),
            'Juego': lambda: self.genCompetencia(self._profesion, "Juego"),
            'Lanzar': lambda: self.genCompetencia(self._profesion, "Lanzar"),
            'LeerEscribir': lambda: self.genCompetencia(self._profesion, "LeerEscribir"),
            'Leyendas': lambda: self.genCompetencia(self._profesion, "Leyendas"),
            'Mando': lambda: self.genCompetencia(self._profesion, "Mando"),
            'Medicina': lambda: self.genCompetencia(self._profesion, "Medicina"),
            'Memoria': lambda: self.genCompetencia(self._profesion, "Memoria"),
            'Musica': lambda: self.genCompetencia(self._profesion, "Musica"),
            'Nadar': lambda: self.genCompetencia(self._profesion, "Nadar"),
            'Navegar': lambda: self.genCompetencia(self._profesion, "Navegar"),
            'Ocultar': lambda: self.genCompetencia(self._profesion, "Ocultar"),
            'Rastrear': lambda: self.genCompetencia(self._profesion, "Rastrear"),
            'Saltar': lambda: self.genCompetencia(self._profesion, "Saltar"),
            'Sanar': lambda: self.genCompetencia(self._profesion, "Sanar"),
            'Seduccion': lambda: self.genCompetencia(self._profesion, "Seduccion"),
            'Sigilo': lambda: self.genCompetencia(self._profesion, "Sigilo"),
            'Teologia': lambda: self.genCompetencia(self._profesion, "Teologia"),
            'Tormento': lambda: self.genCompetencia(self._profesion, "Tormento"),
            'Trepar': lambda: self.genCompetencia(self._profesion, "Trepar"),
            "CompetenciaAuxSlot1": lambda: self.getCompetenciaAux(),
            "CompetenciaAuxSlot2": lambda: self.getCompetenciaAux(),
            "CompetenciaAuxSlot3": lambda: self.getCompetenciaAux(),
            "CompetenciaAuxSlot4": lambda: self.getCompetenciaAux(),
            "CompetenciaAuxSlot5": lambda: self.getCompetenciaAux(),
            "CompetenciaAuxNumSlot1": lambda: random.randint(1, 100),
            "CompetenciaAuxNumSlot2": lambda: random.randint(1, 100),
            "CompetenciaAuxNumSlot3": lambda: random.randint(1, 100),
            "CompetenciaAuxNumSlot4": lambda: random.randint(1, 100),
            "CompetenciaAuxNumSlot5": lambda: random.randint(1, 100),
            "Arcos": lambda: self.genCompetencia(self._profesion, "Arcos"),
            "Ballestas": lambda: self.genCompetencia(self._profesion, "Ballestas"),
            "Cuchillos": lambda: self.genCompetencia(self._profesion, "Cuchillos"),
            "Escudos": lambda: self.genCompetencia(self._profesion, "Escudos"),
            "Espadas": lambda: self.genCompetencia(self._profesion, "Espadas"),
            "Espadones": lambda: self.genCompetencia(self._profesion, "Espadones"),
            "Hachas": lambda: self.genCompetencia(self._profesion, "Hachas"),
            "Hondas": lambda: self.genCompetencia(self._profesion, "Hondas"),
            "Lanzas": lambda: self.genCompetencia(self._profesion, "Lanzas"),
            "Mazas": lambda: self.genCompetencia(self._profesion, "Mazas"),
            "Palos": lambda: self.genCompetencia(self._profesion, "Palos"),
            "Pelea": lambda: self.genCompetencia(self._profesion, "Pelea"),
            # Campos relacionados con armas
            "ArmaNombreSlot1": lambda: self.getArma(1).get("ArmaNombreSlot1", ""),
            "ArmaPorcentajeSlot1": lambda: self.getArma(1).get("ArmaPorcentajeSlot1", ""),
            "ArmaDanoSlot1": lambda: self.getArma(1).get("ArmaDanoSlot1", ""),
            "ArmaTamanoSlot1": lambda: self.getArma(1).get("ArmaTamanoSlot1", ""),
            "ArmaRecargaSlot1": lambda: self.getArma(1).get("ArmaRecargaSlot1", ""),
            "ArmaAlcanceSlot1": lambda: self.getArma(1).get("ArmaAlcanceSlot1", ""),
            "ArmaNotasSlot1": lambda: self.getArma(1).get("ArmaNotasSlot1", ""),

            "ArmaNombreSlot2": lambda: self.getArma(2).get("ArmaNombreSlot2", ""),
            "ArmaPorcentajeSlot2": lambda: self.getArma(2).get("ArmaPorcentajeSlot2", ""),
            "ArmaDanoSlot2": lambda: self.getArma(2).get("ArmaDanoSlot2", ""),
            "ArmaTamanoSlot2": lambda: self.getArma(2).get("ArmaTamanoSlot2", ""),
            "ArmaRecargaSlot2": lambda: self.getArma(2).get("ArmaRecargaSlot2", ""),
            "ArmaAlcanceSlot2": lambda: self.getArma(2).get("ArmaAlcanceSlot2", ""),
            "ArmaNotasSlot2": lambda: self.getArma(2).get("ArmaNotasSlot2", ""),

            "ArmaNombreSlot4": lambda: self.getArma(4).get("ArmaNombreSlot4", ""),
            "ArmaPorcentajeSlot4": lambda: self.getArma(4).get("ArmaPorcentajeSlot4", ""),
            "ArmaDanoSlot4": lambda: self.getArma(4).get("ArmaDanoSlot4", ""),
            "ArmaTamanoSlot4": lambda: self.getArma(4).get("ArmaTamanoSlot4", ""),
            "ArmaRecargaSlot4": lambda: self.getArma(4).get("ArmaRecargaSlot4", ""),
            "ArmaAlcanceSlot4": lambda: self.getArma(4).get("ArmaAlcanceSlot4", ""),
            "ArmaNotasSlot4": lambda: self.getArma(4).get("ArmaNotasSlot4", ""),

            "ArmaNombreSlot5": lambda: self.getArma(5).get("ArmaNombreSlot5", ""),
            "ArmaPorcentajeSlot5": lambda: self.getArma(5).get("ArmaPorcentajeSlot5", ""),
            "ArmaDanoSlot5": lambda: self.getArma(5).get("ArmaDanoSlot5", ""),
            "ArmaTamanoSlot5": lambda: self.getArma(5).get("ArmaTamanoSlot5", ""),
            "ArmaRecargaSlot5": lambda: self.getArma(5).get("ArmaRecargaSlot5", ""),
            "ArmaAlcanceSlot5": lambda: self.getArma(5).get("ArmaAlcanceSlot5", ""),
            "ArmaNotasSlot5": lambda: self.getArma(5).get("ArmaNotasSlot5", ""),

            "IngresoMensual": lambda: self.getIngresoMensual(),
            "Dineros": lambda: self.getDinero(),
            "GastoSemanal": lambda: self.getGasto(),
        }

        # Manejar las descripciones
        if campo.startswith("Descripcion"):
            descripciones = self.situacionFamiliar()
            return descripciones.get(campo, "")

        return handlers.get(campo, lambda: '0')()
