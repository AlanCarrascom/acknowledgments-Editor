import csv                                  # Esta clase permite leer y editar archivos csv
from reportlab.pdfgen.canvas import Canvas  # Esta clase permite la edición de pdf de cero
from reportlab.lib.units import cm, inch    # Esta clase importa las constantes equivalentes en cm e inch

csv_delimiter = ','

with open('nombre_archivo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=csv_delimiter)

canvas = Canvas("nombrePDF.pdf")


