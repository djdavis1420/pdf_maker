from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table, TableStyle
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from resources.styles import styles
from src.file_reader import get_data

doc = SimpleDocTemplate("output/sample.pdf", pagesize=letter, allowSplitting=1)
canvas = canvas.Canvas("output/sample.pdf")

WIDTH, HEIGHT = letter
COLOR = (232 / 256, 79 / 256, 37 / 256)

spacer = Spacer(WIDTH, .25 * inch)
data_set_1 = get_data('DATA1.csv')
data_set_2 = get_data('DATA2.csv')

section_header_style = styles['section_header']
section_header_1 = Paragraph('<b>SECTION HEADER DESCRIBING DATA FORMAT</b>', section_header_style)
section_header_2 = Paragraph('<b>SECTION HEADER DESCRIBING DATA FORMAT</b>', section_header_style)

table_1 = Table(data_set_1, (1.5 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch))
table_1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (6, 0), COLOR),
    ('ALIGN', (0, 0), (6, 0), 'CENTER'),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ('INNERGRID', (0, 0), (-1, -1), 1, COLOR),
    ('BOX', (0, 0), (-1, -1), 1, COLOR)
]))

table_2 = Table(data_set_2, (3.5 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch))
table_2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), COLOR),
    ('ALIGN', (0, 0), (4, 0), 'CENTER'),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ('INNERGRID', (0, 0), (-1, -1), 1, COLOR),
    ('BOX', (0, 0), (-1, -1), 1, COLOR)
]))

story = []
story.append(spacer)
story.append(spacer)
story.append(spacer)
story.append(section_header_1)
story.append(spacer)
story.append(table_1)
story.append(spacer)
story.append(spacer)
story.append(section_header_2)
story.append(spacer)
story.append(table_2)


def FirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 18)
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - .70 * inch, '{{Name of Client}}')
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - .95 * inch, 'Project Status Report')
    canvas.drawString(WIDTH - 8.0 * inch, HEIGHT - 1.20 * inch, '{{Timeframe for Report}}')
    image_path = "resources/images/generic_logo.jpg"
    canvas.drawImage(image_path, WIDTH - 2.5 * inch, HEIGHT - 1.25 * inch, width=2 * inch, height=.86 * inch)
    canvas.setLineWidth(5)
    canvas.setStrokeColorRGB(232 / 256, 79 / 256, 37 / 256, 1.0)
    canvas.line(.5 * inch, HEIGHT - 1.55 * inch, 8 * inch, HEIGHT - 1.55 * inch)
    canvas.restoreState()


doc.build(story, onFirstPage=FirstPage)
