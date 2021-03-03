# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# https://mouseinfo.readthedocs.io/en/latest/
# https://readthedocs.org/projects/pyautogui/downloads/pdf/latest/
# https://myrusakov.ru/python-gui-automation.html
# https://medium.com/nastia-shu/%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5-%D0%BD%D0%B5-%D0%BD%D1%83%D0%B6%D0%BD%D0%BE-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D1%81%D0%BE%D1%82%D0%BD%D0%B8-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%B2-excel-e0a1f5a9e9a7
# Автоматизация Excel с помощью Python nastia shu
# https://pyautogui.readthedocs.io/en/latest/source/modules.html
# https://pyautogui-ru.readthedocs.io/ru/latest/
# https://cyberguru.tech/программирование/python/pyautogui
# https://cyberguru.tech/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/python/pyautogui

import pyautogui
pyautogui.PAUSE = 0.5
qwerty = """qwertyuiop[]asdfghjkl;'zxcvbnm,.?/QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""
ycuken = """йцукенгшщзхъфывапролджэячсмитьбю,.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"""
tr = dict(zip(ycuken, qwerty))

def translate(key):
    """Returns qwerty key or the given key itself if no mapping found"""
    return "".join(map(lambda x: tr.get(x, x), key))

pyautogui.alert('raImya быть на экране OK button.')
noteX, noteY = pyautogui.locateCenterOnScreen('eraImya.png')
print(noteX, noteY)
pyautogui.moveTo(noteX, noteY, duration=1)
pyautogui.hotkey('ctrl', 'shift') #ru/en click, all mark, rewrite ru/en
pyautogui.click(); pyautogui.hotkey('ctrl', 'a'); pyautogui.write(translate('Павел Владимирович Падерин'), 0.15)
pyautogui.hotkey('ctrl', 'shift')

# pyautogui.click(noteX, noteY); pyautogui.write(translate('Павел Владимирович Падерин'), 0.15)
# pyautogui.hotkey('ctrl', 'shift')
# pyautogui.mouseInfo()
# pyautogui.write('Павел Pavel Vladimirovich Paderin', 0.15)
# pyautogui.click(); pyautogui.write('Павел Владимирович Падерин', 0.25)
# pyautogui.alert('Блокнот должен быть на экране OK button.')
# noteX, noteY = pyautogui.locateCenterOnScreen('notepadPNG.png')
# pyautogui.moveTo(noteX, noteY + 20, duration=1) # только двумя командами
# pyautogui.click()                               # и этой
# pyautogui.typewrite(str(pyautogui.position()) + '\n', interval=0.1)
# import pip
# pip install pyautogui
# pyautogui.click(noteX, noteY + 20, duration=1)
# screenWidth, screenHeight = pyautogui.size() # Получаем размер экрана.
# print(pyautogui.size())
# print(screenWidth,screenHeight)
# print(pyautogui.locateCenterOnScreen('notepadPNG.png'))
# pyautogui.moveTo(165, 460, duration=2)
# pyautogui.moveRel(note_Center, duration=5)
# pyautogui.moveTo(165, 460, duration=1.2)
# print(pyautogui.position())
# pyautogui.moveTo(165, 460, duration=2)
# pyautogui.click(x=50, y=365, clicks=1, interval=3, button='left')
# pyautogui.rightClick(x=50, y=365, interval=3, duration=2)
# pyautogui.typewrite('Hello02!\n', interval=0.1)
# print(pyautogui.position())
# pyautogui.typewrite(str(pyautogui.position()) + '\n', interval=0.1)
# pyautogui.confirm('This displays text and has an OK and Cancel button.')
# pypromt = pyautogui.prompt('This lets the user type in a string and press OK.')
# pyautogui.typewrite(str(pypromt) + '\n', interval=0.1)
# print(pypromt)
# pyautogui.moveTo(noteX, noteY + 20, 6, pyautogui.easeInElastic)
