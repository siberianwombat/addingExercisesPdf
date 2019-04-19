from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import pagesizes


c = canvas.Canvas("test.pdf", bottomup=0)
pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
c.setFont("Verdana", 20)

p = Paragraph("test <font size=30>test</font> test", ParagraphStyle('parrafos',
                           fontSize = 20))
p.wrap(300, 300)
p.drawOn(c, 200, 200)
c.save()