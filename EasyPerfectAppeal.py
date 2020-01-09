# coding: utf-8
import time
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
import pyautogui
import ctypes

#タイミング定数
MENTAL_100 = 1.35
MENTAL_90 = 1.235
MENTAL_70 = 1.2
MENTAL_50 = 1.104
MENTAL_20 = 0.99

#アピールバー閾値定数
THRESHOLD_1 = 0.91
THRESHOLD_2 = 0.71
THRESHOLD_3 = 0.51
THRESHOLD_4 = 0.1

#自動クリック関数
def perfect_click(timing):
    pyautogui.click()
    time.sleep(timing)
    pyautogui.click()

    #メンタル値入力関数
def mental_input():
    #mental_maximum = input('メンタル値 -> ')
    mental_maximum = 2179
    try:
        mental_maximum = float(mental_maximum)
        mental = {'threshold91' : int(mental_maximum * THRESHOLD_1),\
                'threshold71' : int(mental_maximum * THRESHOLD_2),\
                'threshold51' : int(mental_maximum * THRESHOLD_3),\
                'threshold10' : int(mental_maximum * THRESHOLD_4)}
        display_message(mental)
    except:
        print('数字を入力してね')
        mental_input()

    #メッセージ表示関数
def display_message(mental):
    print('\n*****************************************')
    print('\n攻撃対象にカーソル合わせてキーを押してね\n')
    print('Alt + 1  ..  %d↑'%mental['threshold91'])
    print('Alt + 2  ..  %d↑'%mental['threshold71'])
    print('Alt + 3  ..  %d↑'%mental['threshold51'])
    print('Alt + 4  ..  %d↑'%mental['threshold10'])
    print('Alt + 5  ..  ~0\n')
    print('Alt + Q  ..  メンタル再入力')
    print('esc      ..  終了')
    print('\n動作中........')

################################################################
################################################################
################################################################

mental_input()

while True:
    #0x12..Altキー 0x31~..12345 0x51..Q
    if(ctypes.windll.user32.GetAsyncKeyState(0x31)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        perfect_click(MENTAL_100)
    if(ctypes.windll.user32.GetAsyncKeyState(0x32)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        perfect_click(MENTAL_90)
    if(ctypes.windll.user32.GetAsyncKeyState(0x33)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        perfect_click(MENTAL_70)
    if(ctypes.windll.user32.GetAsyncKeyState(0x34)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        perfect_click(MENTAL_50)
    if(ctypes.windll.user32.GetAsyncKeyState(0x35)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        perfect_click(MENTAL_20)
    if(ctypes.windll.user32.GetAsyncKeyState(0x51)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        pyautogui.press('esc')#おかしい
        mental_input()
    if(ctypes.windll.user32.GetAsyncKeyState(0x1B)&0x8000):
        break