from fillpdf import fillpdfs
from funciones import GeneradorPersonaje
from form_fields import form_fields

def generar_ficha():
    """
    Genera los valores de los campos en el orden especificado en form_fields.
    """
    generador = GeneradorPersonaje()
    excluidos = {'Herido', 'Malherido', 'Inconsciente', 'Muerto'}  # Campos que no se deben generar

    # Generar los valores en el orden de form_fields
    datos = {}
    for campo in form_fields:
        if campo not in excluidos:
            valor = generador.generar_valor(campo)
            datos[campo] = valor

    # Escribir los valores en el PDF
    fillpdfs.write_fillable_pdf(
        'HojaAquelarrePlantilla.pdf',
        'Hoja_Personaje_Rellena.pdf',
        datos
    )
    return datos

if __name__ == "__main__":
    print("Generando ficha optimizada...")
    ficha = generar_ficha()
    print("Ficha generada con éxito!")