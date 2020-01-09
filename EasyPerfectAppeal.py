# coding: utf-8
import time
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
import pyautogui
import ctypes
#タイミング定数
MENTAL_100 = 1
MENTAL_90 = 0.9
MENTAL_70 = 0.7
MENTAL_50 = 0.5
MENTAL_20 = 0.3

def perfect_click(timing):
    pyautogui.click()
    time.sleep(timing)
    pyautogui.click()

print('\n攻撃対象にカーソル合わせてキーを押してね\n')
print('1    .. max')
print('2    .. 90%↓')
print('3    .. 70%↓')
print('4    .. 50%↓')
print('5    .. 10%↓')
print('esc  .. 終了')
print('\n動作中........')

while True:
    if(ctypes.windll.user32.GetAsyncKeyState(0x31)&0x8000):
        perfect_click(MENTAL_100)
    if(ctypes.windll.user32.GetAsyncKeyState(0x32)&0x8000):
        perfect_click(MENTAL_90)
    if(ctypes.windll.user32.GetAsyncKeyState(0x33)&0x8000):
        perfect_click(MENTAL_70)
    if(ctypes.windll.user32.GetAsyncKeyState(0x34)&0x8000):
        perfect_click(MENTAL_50)
    if(ctypes.windll.user32.GetAsyncKeyState(0x35)&0x8000):
        perfect_click(MENTAL_20)
    if(ctypes.windll.user32.GetAsyncKeyState(0x1B)&0x8000):
        break