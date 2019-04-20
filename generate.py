import random
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import pagesizes

font = "Helvetica"
fontSize = 20
placeholderHeight = 30
placeholderWidth = 40
marginX = 10

def randomAddition():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return f'{a:d} + {b:d} ='

def randomSubstraction():
    a = random.randint(3, 19)
    b = random.randint(1, min(5, a-1))
    return f'{a:d} — {b:d} ='

def randomAdditionSubstraction():
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(1, min(5, a + b))
    return f'{a:d} + {b:d} — {c:d} ='

def lessOrMore():
    a = random.randint(0, 20)
    if random.randint(0, 100) < 30: # 30% is 'equal' 
        b = a
    else:
        b = random.randint(0, 20)
    return f'{a:d} ▢ {b:d}'

def placeholderAdditionA():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a + b
    return f'▢ + {a:d} = {c:d}'

def placeholderAdditionB():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a + b
    return f'{a:d} + ▢ = {c:d}'

def placeholderSubstractionA():
    a = random.randint(3, 19)
    b = random.randint(1, min(5, a-1))
    c = a - b
    return f'▢ — {b:d} = {c:d}'

def placeholderSubstractionB():
    a = random.randint(3, 19)
    b = random.randint(1, min(5, a-1))
    c = a - b
    return f'{a:d} — ▢ = {c:d}'

def placeholderSimple():
    exersise = {
        1: placeholderAdditionA,
        2: placeholderAdditionB,
        3: placeholderSubstractionA,
        4: placeholderSubstractionB,
    }.get(random.randint(1,4))
    return exersise()

def drawPlaceholders(canvas, x, y, str, placeHolderX, placeHolderY, font, fontSize):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    placeholderChar = '▢'
    substrings = str.split(placeholderChar)
    needPlaceholder = 0 
    curX = x
    for substring in substrings:
        if needPlaceholder: 
            canvas.roundRect(curX, y - fontSize, placeHolderX, placeHolderY, 5, stroke=1, fill=0)
            curX += placeHolderX
        canvas.drawString(curX, y, substring)
        indent = stringWidth(substring, font, fontSize)
        curX += indent
        needPlaceholder = 1    

examplesSwitcher = {
    1: randomAddition,
    2: randomSubstraction,
    3: randomAdditionSubstraction,
    4: lessOrMore,
    5: placeholderSimple,
}

table = []
nRows = 14
nCols = 2
(a4WidthPoints, a4HeightPoints) = pagesizes.A4

for r in range(nRows):
    row = []
    for c in range(nCols):
        sampleGenerator = examplesSwitcher.get(random.randint(5,5), lambda: "Invalid value")
        row.append(sampleGenerator())
    table.append(row)

for line in table:
    print ("", line)

c = canvas.Canvas("samples.pdf", bottomup=0)
c.setFont(font, fontSize)
# pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
# c.setFont("Verdana", 20)

stepY = int(a4HeightPoints / (nRows + 1))
stepX = int(a4WidthPoints / nCols)
cursorY = stepY
for line in table:
    cursorX = 0
    for cell in line:
        drawPlaceholders(c, cursorX + marginX, cursorY, cell, placeholderWidth, placeholderHeight, font, fontSize)
        cursorX += stepX
    cursorY += stepY
c.save()
