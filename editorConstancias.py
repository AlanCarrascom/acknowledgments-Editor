'''
Title:  Python Acknowledgment Editor
Author: Alan Carrasco
Date:   21/sep/2023
'''

import csv                                                                  # Esta clase permite leer y editar archivos csv
from reportlab.pdfgen.canvas import Canvas                                  # Esta clase permite la edición de pdf de cero
from reportlab.lib.units import mm, cm, inch                                # Esta clase importa las constantes equivalentes en cm e inch
from reportlab.lib.colors import black, goldenrod, darkblue, royalblue      # Esta clase importa los colores para el texto

############################
#
#   Cuando acabes con el diseño
#   ordena estas constantes
#
############################

csv_delimiter = ','                        # Delimitador del csv, puede ser ',', ';' o '.'
csv_filename = 'nombre_archivo.csv'        # Especificar el nombre del archivo

ancho_constancia = 1080 * mm               # Especifica el ancho de la constancia
alto_constancia = 1080 * mm                # Especifica el ancho de la constancia

ancho_barras = 25 * mm

headers = True                             # True si el csv tiene títulos, False si no tiene títulos.

logoFI = "Logos/escudofi_azul.jpg"         # Ubicación de logo FI
anchoFI = 153*mm
altoFI = 182*mm

logoUNAM = "Logos/escudounam_azul.jpg"     # Ubicación de logo UNAM
anchoUNAM = 155*mm
altoUNAM = 174*mm

logoPROTECO = "Logos/logoPROTECO.jpeg"
anchoPROTECO = 1027*mm
altoPROTECO = 716*mm

logos_border_padding = 22*mm
y_logos = 778*mm

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
canvas.rect(0, ancho_barras, ancho_constancia, ancho_barras, stroke=0, fill=1)
canvas.rect(0, alto_constancia-2*ancho_barras, ancho_constancia, ancho_barras, stroke=0, fill=1)

# Logo PROTECO
canvas.drawImage(logoPROTECO, 27*mm, 159*mm, anchoPROTECO, altoPROTECO)

# Barras azules superior e inferior
canvas.setFillColor(darkblue)
canvas.rect(0, alto_constancia - ancho_barras, ancho_constancia, ancho_barras, stroke=0, fill=1)
canvas.rect(0, 0, ancho_constancia, ancho_barras, stroke=0, fill=1)

# Logos FI y UNAM
canvas.drawImage(logoUNAM, logos_border_padding, y_logos, anchoUNAM, altoUNAM)
canvas.drawImage(logoFI, ancho_constancia - logos_border_padding - anchoFI, y_logos, anchoFI, altoFI)

# Cadenas del certificado
# Universidad
canvas.setFont("Times-Roman", 80)
canvas.setFillColor(black)
canvas.drawString(200*mm, 911*mm, "UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO")
canvas.setFont("Times-Roman", 75)
canvas.drawString(400*mm, 870*mm, "FACULTAD DE INGENIERÍA")
canvas.setFont("Times-Roman", 60)
canvas.drawString(378*mm, 835*mm, "DIVISIÓN DE INGENIERÍA ELÉCTRICA")
canvas.drawString(382*mm, 805*mm, "DEPARTAMENTO DE COMPUTACIÓN")

# Constancia
canvas.setFillColor(darkblue)
canvas.setFont("Times-Roman", 120)
canvas.drawString(420*mm, 730*mm, "CONSTANCIA")

canvas.save()
