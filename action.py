import win32gui, pydirectinput, pythoncom
import pyautogui
import time
from pywinauto.application import Application
from pywinauto import findwindows
from config import *

class Action():
    def __init__(self):
        super().__init__()
        self.exe_path = exe_path
        self.loading = 0

    # 啟動模擬器多開
    def open_muilty_manager(self):
        app = Application().start(self.exe_path)

    # 確認模擬器開啟

    # 模擬器啟動遊戲
    def emulator_start_up(self):
        print('模擬器啟動遊戲')
        self.process_to_front('雷電多開器')
        img_location = pyautogui.locateOnScreen(image='img/emulator_manager/001_start_up.png')

        if img_location:
            x, y = pyautogui.center(img_location)
            x += 482
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.click()
            self.loading = 1
            print('emulator_start_up...')

    # 程序拉至最前
    def process_to_front(self, process):
        hwnd = win32gui.FindWindow(None, process)
        win32gui.SetForegroundWindow(hwnd)

    # 確認程序執行
    def is_process_running(self, process_name):
        # windows = findwindows.find_element(class_name='#32770', title_re = process_name)
        windows = findwindows.find_element(title_re = process_name)

        if windows and windows[0].is_visible():
            return True
        return False

    # 開啟楓M(模擬器桌面)
    def start_mapleM(self):
        img_location = pyautogui.locateOnScreen(image='img/emulator/001_icon.png')
        print(img_location)

        if img_location:
            x, y = pyautogui.center(img_location)
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.click()
            print('open mapleM now...')
        else:
            print('error in start_mapleM')

    # 等待
    def standby(self, second = 5):
        print(f'waiting {second} seconds')
        time.sleep(second)
        print(f'waiting finished')

    # 滑鼠當前座標
    def mouse_posotion():
        while True:
            x, y = pyautogui.position()
            print(x, y)
    # mouse_posotion()

    # 登入頁面


