# coding: utf-8
import win32gui
import win32con
import pyautogui
from PIL import ImageGrab
from PIL import Image
import numpy as np
import ctypes

#基幹部
def auto_perfect_appeal():
    hwnd = win32gui.GetForegroundWindow()
    capture_position = get_capture_position(hwnd)
    img = capture_screen(capture_position)
    print(perfect_calc(img,img.shape[0]))

#キャプチャ座標取得
def get_capture_position(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x1 = rect[0] + 9
    y1 = rect[1] + 9
    x2 = rect[2] - 9
    y2 = rect[3] - 9
    return [x1,y1,x2,y2]

#実際にキャプチャ
def capture_screen(capture_position):
    grabed_image = ImageGrab.grab()
    trimmed_image = grabed_image.crop(capture_position)
    #trimmed_image.save('test.jpg')
    return np.asarray(trimmed_image)

#PERFECTピクセル数算出
def perfect_calc(img, array_size):
    true_amount = 0
    for num in range(array_size):
        tmp_list = np.all(img[num] == 255, axis=1).tolist()
        true_amount += tmp_list.count(True)
    else:
        return true_amount

############################################################
############################################################
############################################################

#0x12..Altキー 0x31~..12345 0x51..Q
while True:
    if(ctypes.windll.user32.GetAsyncKeyState(0x31)&ctypes.windll.user32.GetAsyncKeyState(0x12)&0x8000):
        auto_perfect_appeal()
    if(ctypes.windll.user32.GetAsyncKeyState(0x1B)&0x8000):
        break