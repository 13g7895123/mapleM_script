import win32gui, pydirectinput, pythoncom
import pyautogui
import time

# 確認模擬器開啟

# 模擬器啟動遊戲
def emulator_start_up():
    img_location = pyautogui.locateOnScreen(image='MapleM/img/emulator/001_start_up.png')

    if img_location:
        x, y = pyautogui.center(img_location)
        x += 482
        pyautogui.moveTo(x, y, duration=1)
emulator_start_up()

# 程序拉至最前
def process_to_front(process):
    hwnd = win32gui.FindWindow(None, process)
    win32gui.SetForegroundWindow(hwnd)


# 開啟楓M(模擬器桌面)
def start_mapleM():
    img_location = pyautogui.locateOnScreen(image='img/001.png')
    print(img_location)

    if img_location:
        x, y = pyautogui.center(img_location)
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
        print('open mapleM now...')
    else:
        print('error in start_mapleM')

# 等待
def standby(second = 5):
    time.sleep(second)

# 滑鼠當前座標
def mouse_posotion():
    while True:
        x, y = pyautogui.position()
        print(x, y)
# mouse_posotion()

# 登入頁面
