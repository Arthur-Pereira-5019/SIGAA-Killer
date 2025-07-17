import string
import time

import pyautogui as py
import time as t
import winsound
import pyperclip as cb
import sys
import os

# Basic settings


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

i = 0
fileName = ''
currentDiscipline = ''
ended = False
print("Começou! Sigaa Killer 1.0 por Arthur Pereira a.k.a. Art5019")

def returnHome():
    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/homebutton.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            t.sleep(0.5)
    py.click(x, y)

def returnAbsences(results):
    lines = results.splitlines()
    absences = (lines[0].rsplit(": ")[1])
    maximum = lines[1].rsplit(": ")[1]

    global currentDiscipline
    print("O número de faltas na disciplina " + currentDiscipline + " é " + absences + "/" + maximum)
    returnHome()

def extractAbsencesUsingCursor():
    canSkip = False
    while not canSkip:
        try:
            a = py.locateOnScreen(resource_path('images/abscensesfileref.png'),grayscale=True)

            canSkip = True
        except Exception as e:
            t.sleep(0.5)

    py.click(a.left, a.top)
    py.keyDown('shift')
    py.click(a.left+a.width + a.width/2, a.top+a.height)
    py.keyUp('shift')
    py.hotkey('ctrl', 'c')

    returnAbsences(cb.paste())


def rollDown():
    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/mapadefrequencia.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            t.sleep(0.5)

    py.click(x, y)
    py.scroll(-2000)
    extractAbsencesUsingCursor()


def getDisciplineName():
    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/refdiscipline.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            time.sleep(0.5)

    py.click(x, y+50)
    py.click(x, y+50)
    py.click(x, y+50)
    py.hotkey('ctrl', 'c')
    global currentDiscipline
    currentDiscipline = cb.paste()


def hasNext(x, y):
    cb.copy('')
    py.click(x,y)
    py.click(x,y)
    py.click(x,y)
    py.hotkey('ctrl', 'c')
    if 'turma' in cb.paste():
        global ended
        ended = True
        return False
    return True


def goToFrequncy():
    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/componente.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            time.sleep(0.5)
            print(e)

    py.click(x, y)
    py.scroll(-340)

    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/componente.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            time.sleep(0.5)

    if not hasNext(x - 200, y + 10 + ((i+1)*28)):
        return

    t.sleep(0.5)
    getDisciplineName()

    canSkip = False
    while not canSkip:
        try:
            x, y = py.locateCenterOnScreen(resource_path('images/frequencia.png'), grayscale=True)
            canSkip = True
        except Exception as e:
            try:
                x, y = py.locateCenterOnScreen(resource_path('images/alunos.png'), grayscale=True)
                py.click(x, y)
            except Exception as b:
                time.sleep(1)

    py.click(x, y)
    t.sleep(0.5)
    rollDown()

temp = cb.paste
while not ended:
    goToFrequncy()
    i += 1
cb.copy = cb.paste

winsound.Beep(500, 1000)

input("Press Enter to exit...")