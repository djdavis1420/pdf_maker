from reportlab.lib.styles import ParagraphStyle

styles = {
    'main_header': ParagraphStyle(
        'default',
        fontName='Helvetica',
        fontSize=15,
        leading=-1,
        leftIndent=-40,
        spaceBefore=20,
        spaceAfter=20,
        textColor=(232 / 256, 79 / 256, 37 / 256)
    ),
    'section_header': ParagraphStyle(
        'default',
        fontName='Helvetica',
        leftIndent=-40,
        fontSize=15,
        textColor=(232 / 256, 79 / 256, 37 / 256)
    )
}
