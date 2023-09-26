'''
Title:  Python Acknowledgment Editor
Author: Alan Carrasco
Date:   25/sep/2023
'''

# Talvez sea necesario que se instale reportlab para poder correr el script

import csv                                                                  # Esta biblioteca permite leer y editar archivos csv
import os                                                                   # Esta biblioteca permite interactuar con el OS
from reportlab.pdfgen.canvas import Canvas                                  # Esta clase permite la edición de pdf de cero
from reportlab.lib.units import mm, inch                                    # Esta clase importa las constantes equivalentes en cm e inch
from reportlab.pdfbase.pdfmetrics import stringWidth                        # Esta función retorna el tamaño de que tendría un texto
from reportlab.lib.colors import black                                      # ESta constante es el valor rgb de un color

# Función para limpiar cadenas
def clean_string(string:str) -> str:
  special_chars = 'áéíóú¿?¡!.,;:-_'
  replacement_special_chars = 'aeiou          '
  translation_table = str.maketrans(special_chars,replacement_special_chars)
  formated_string = string.translate(translation_table).lower()
  return formated_string

csv_delimiter = ','                                 # Delimitador del csv, puede ser ',', ';' o '.'
csv_filename = 'Usuarios/datosConstancias.csv'      # Ubicación del CSV
plantilla = "Logos/plantillaConstancia.png"         # Ubicación de la plantilla de constancia

ancho_constancia = 1080 * mm               # Especifica el ancho de la constancia
alto_constancia = 1080 * mm                # Especifica el ancho de la constancia

with open(csv_filename, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=csv_delimiter)
    for usuario in csv_reader:

        # Valores
        nombre = usuario[0]
        curso = usuario[1]
        fechaInicio = usuario[2]
        fechaFin = usuario[3]

        # Plantilla
        nombreLimpio = clean_string(nombre)
        contador = 0
        while os.path.exists(f"{nombreLimpio}_constancia2024-1_{contador}.pdf"):
           contador+=1
        canvas = Canvas(f"{nombreLimpio}_constancia2024-1_{contador}.pdf")
        canvas.setPageSize((ancho_constancia, alto_constancia))
        canvas.drawImage(plantilla, 0, 0, ancho_constancia, alto_constancia)
        canvas.setFillColor(black)

        # Nombre
        canvas.setFont("Times-Roman", 100)
        nameLength = stringWidth(nombre, 'Times-Roman', 100)
        y_nombre = 560*mm
        canvas.drawString((ancho_constancia - nameLength)/2, y_nombre, nombre)

        # Curso
        cursoLength = stringWidth(curso, 'Times-Roman', 100)
        y_curso = 470*mm
        canvas.drawString((ancho_constancia - cursoLength)/2, y_curso, curso)

        # Fechas
        canvas.setFontSize(17*mm)
        y_fecha = 421*mm
        canvas.drawString(346*mm, y_fecha, fechaInicio)
        canvas.drawString(443*mm, y_fecha, fechaFin)

        tipoCurso = 'CI'
        semestre = '2024-1'
        categoria = 'B'
        curso = clean_string(curso)
        if ('intermedio' in curso or '2' in curso or 'ii' in curso or 'll' in curso):
           categoria = 'I'
        elif ('avanzado' in curso or '3' in curso or 'iii' in curso):
           categoria = 'A'
        serial_code = f'{tipoCurso}-{semestre}-{categoria}'

        # Codigos de serie
        canvas.setFontSize(20*mm)
        codeLength=stringWidth(serial_code,'Times-Roman', 20*mm)
        canvas.drawString(ancho_constancia - codeLength - mm, 1.7*inch, serial_code)

        # Guardar el PDF generado
        canvas.showPage()
        canvas.save()
