import string
import time

import pyautogui as py
import pyscreeze
import time as t
from PIL import Image
import pytesseract
import os

i = 0;
if not os.path.isdir('generated'):
    os.mkdir('generated')

# Open the discipline
a = py.locateOnScreen('componente.png')
x, y = py.center(a)
py.click(x - 90, y + 25)

# Go for the "Alunos" tab
# t.sleep(2)
# canSkip = False;
# while not canSkip:
    # try:
        # a = py.locateOnScreen('alunos.png')
        # canSkip = True
    # except Exception as e:
        # print('Is your internet slow or there is some problem with your screen? Not found the Alunos button. Trying again in 3 seconds')
        # time.sleep(3)

# x, y = py.center(a)
# py.click(x,y)

t.sleep(0.5)
canSkip = False;
while not canSkip:
    try:
        a = py.locateOnScreen('frequencia.png')
        canSkip = True
    except Exception as e:
        print('Is your internet slow or there is some problem with your screen? Not found the Frequencia button. Trying again in 0.5 seconds')
        t.sleep(1)

x, y = py.center(a)
py.click(x, y)
t.sleep(0.5)

canSkip = False
while not canSkip:
    try:
        a = py.locateOnScreen('mapadefrequencia.png')
        canSkip = True
    except Exception as e:
        print('Is your internet slow or there is some problem with your screen? Not found the Abscences table. Trying again in 0.5 seconds')
        t.sleep(0.5)

x, y = py.center(a)
py.click(x,y)
py.scroll(-400)

canSkip = False
while not canSkip:
    try:
        a = py.locateOnScreen('abscensesfileref.png')
        canSkip = True
    except Exception as e:
        print('Is your internet slow or there is some problem with your screen? Not found the Abscences table. Trying again in 0.5 second')
        t.sleep(0.5)

printName = 'generated/disciplina' + i.__str__() + '.png'
absencesBox = (a.left, a.top, a.width + int(a.width/1.5), a.height)
py.screenshot(printName, absencesBox)






