'''
Title:  Python Acknowledgment Editor
Author: Alan Carrasco
Date:   21/sep/2023
'''

import csv                                  # Esta clase permite leer y editar archivos csv
from reportlab.pdfgen.canvas import Canvas  # Esta clase permite la edición de pdf de cero
from reportlab.lib.units import mm, cm, inch    # Esta clase importa las constantes equivalentes en cm e inch
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.colors import black, goldenrod, darkblue      # Esta clase importa los colores para el texto

csv_delimiter = ','                         # Delimitador del csv, puede ser ',', ';' o '.'
csv_filename = 'nombre_archivo.csv'         # Especificar el nombre del archivo
ancho_constancia = 286 * mm                 # Especifica el ancho de la constancia
alto_constancia = 286 * mm                  # Especifica el ancho de la constancia
headers = True                              # True si el csv tiene títulos, False si no tiene títulos.

'''
with open(csv_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=csv_delimiter)
    line_count = 0
    
    for row in csv_reader:
        if headers == True and line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1

        # Aquí se debe escribir todo lo que se quiere hacer con el archivo
'''

canvas = Canvas("samplePDF.pdf")
canvas.setPageSize((ancho_constancia, alto_constancia))
canvas.setFont("Times-Roman", 18)    # Fuentes disponibles: Courier, Helvetica y Times-Roman

# Barras amarillas superior e inferior
canvas.setFillColor(goldenrod)
canvas.rect(0, 0.25*inch, ancho_constancia, 0.25 * inch, stroke=0, fill=1)
canvas.rect(0, alto_constancia-0.5*inch, ancho_constancia, 0.25*inch, stroke=0, fill=1)

# Barras azules superior e inferior
canvas.setFillColor(darkblue)
canvas.rect(0, alto_constancia-0.25*inch, ancho_constancia, 0.25*inch, stroke=0, fill=1)
canvas.rect(0, 0, ancho_constancia, 0.25*inch, stroke=0, fill=1)

# Logos FI y UNAM


#Logo Proteco


canvas.save()
