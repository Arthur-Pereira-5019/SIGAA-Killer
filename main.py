import string
import time

import pyautogui as py
import pyscreeze
import time as t
from PIL import Image
import pytesseract as ts
import os
import winsound

# Basic settings
ts.pytesseract.tesseract_cmd = 'tesseract/tesseract.exe'

if not os.path.isdir('generated'):
    os.mkdir('generated')

i = 0
fileName = ''
atualDisciplina = ''

# Open the discipline

def textTreatment(a):
    match a:
        case ("B"):
            return "8"
    return a

def returnAbsences():
    results = ts.image_to_string(fileName, 'eng')

    absences = results.rsplit(": ")[1].rsplit("\n")[0]
    maximum = results.rsplit(": ")[2]
    absences = textTreatment(absences)
    maximum = textTreatment(maximum)
    global i
    if not absences.isnumeric:
        print("Não foi possível achar o número de faltas na disciplina " + i.__str__())
    if not absences.isnumeric:
        print("Não foi possível achar o número máximo de faltas na disciplina " + i.__str__())
    print("O número de faltas na disciplina é " + absences.__str__() + "/" + maximum.__str__())


def findAndPrintAbsencesBox():
    canSkip = False
    while not canSkip:
        try:
            a = py.locateOnScreen('abscensesfileref.png')
            canSkip = True
        except Exception as e:
            t.sleep(0.5)

    global fileName
    fileName = 'generated/disciplina' + i.__str__() + '.png'
    absencesBox = (a.left, a.top, a.width + int(a.width / 1.5), a.height)
    py.screenshot(fileName, absencesBox)
    returnAbsences()

def rollDown():
    canSkip = False
    while not canSkip:
        try:
            a = py.locateOnScreen('mapadefrequencia.png')
            canSkip = True
        except Exception as e:
            t.sleep(0.5)

    x, y = py.center(a)
    py.click(x, y)
    py.scroll(-400)
    findAndPrintAbsencesBox()

def hasNext():
    py.click()
    py.click()
    py.click()
    py.hotkey('ctrl', 'shift', 'c')


def goToFrequncy():
    a = py.locateOnScreen('componente.png')
    x, y = py.center(a)
    py.click(x - 90, y + 25)

    t.sleep(0.5)
    canSkip = False;
    while not canSkip:
        try:
            a = py.locateOnScreen('frequencia.png')
            canSkip = True
        except Exception as e:
            try:
                a = py.locateOnScreen('alunos.png')
                x, y = py.center(a)
                py.click(x, y)
            except Exception as b:
                time.sleep(1)

    x, y = py.center(a)
    py.click(x, y)
    t.sleep(0.5)
    rollDown()


goToFrequncy()

winsound.Beep(500, 1000)