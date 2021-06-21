import pyautogui
import time
import random
import math

z = 1
list1 = [1137, 70, 1131, 98, 1106, 73, 1104, 100, 1079, 70, 1045, 98, 997, 78]
# 884, 81, 1033, 79, 1043, 79
# 1083, 72, 110, 70, 1081, 107, 1052, 76, 1050, 101, 919, 75, 967, 77, 1134, 74, 1133, 96, 1104, 96, 944, 76
i = 0
time.sleep(2)
pyautogui.press('win')
time.sleep(0.2)
pyautogui.write('paint', interval=0.5)
time.sleep(0.2)
pyautogui.press('enter')
pyautogui.moveTo(730, 80, 2)
pyautogui.click()
time.sleep(0.2)
pyautogui.move(0, 250, 1)
pyautogui.click()
time.sleep(1)
r = 300
x = 960
y = 540
pyautogui.moveTo(x, y, 1)
pyautogui.drag(r, 0, 0.5)
pyautogui.moveTo(x, y)
pyautogui.drag(-r, 0, 0.5)
pyautogui.moveTo(x, y)
pyautogui.drag(0, r, 0.5)
pyautogui.moveTo(x, y)
pyautogui.drag(0, -r, 0.5)
time.sleep(1)
while z == 1:
    theta = round(random.uniform(0, 2 * math.pi), 5)
    a = 960 - round(300 * math.cos(theta), 5)
    b = 540 - round(300 * math.sin(theta), 5)
    p = list1[i]
    q = list1[i + 1]
    if i % 2 != 0:
        i = i + 1
        continue
    pyautogui.moveTo(p, q, 0.1)
    pyautogui.click()
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(a, b)
    if i >= len(list1) - 2:
        i = 0
    else:
        i = i + 1
