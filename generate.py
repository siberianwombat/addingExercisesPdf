import random
from reportlab.pdfgen import canvas


def randomAddition():
    a = random.randint(1,10)
    b = random.randint(1,10)
    return f'{a:d} + {b:d} ='

def randomSubstraction():
    a = random.randint(3,19)
    b = 20 
    while b >= a:
        b = random.randint(1,10)
    return f'{a:d} — {b:d} ='

examplesSwitcher = {
    1: randomAddition,
    2: randomSubstraction
}

table = []
nRows = 14
nCols = 2
a4WidthPoints = 595
a4HeightPoints = 842 

for r in range(nRows):
    row = []
    for c in range(nCols):
        sampleGenerator = examplesSwitcher.get(random.randint(1,len(examplesSwitcher)), lambda: "Invalid value")
        row.append(sampleGenerator())
    table.append(row)

for line in table:
    print ("", line)

c = canvas.Canvas("samples.pdf", bottomup=0)
c.setFont('Helvetica', 20)
stepY = int(a4HeightPoints / (nRows + 1))
stepX = int(a4WidthPoints / nCols)
marginX = 10
cursorY = stepY
for line in table:
    cursorX = 0
    for cell in line:
        print (f"{cursorX:3}:{cursorY:3} -> cell")
        c.drawString(cursorX + marginX, cursorY, cell)
        cursorX += stepX
    cursorY += stepY
c.save()
