import pyautogui as py
import pyscreeze


i = 0

a = py.locateOnScreen('componente.png')

x, y = py.center(a)

py.click(x-90, y+25)
print(x, y)
