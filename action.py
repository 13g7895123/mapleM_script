import win32gui
import pydirectinput
import pythoncom
import pyautogui
import time
import pygetwindow
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
        img_path = 'img/emulator/001_icon.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('open mapleM now...')
        else:
            print('error in start_mapleM')

    # 關閉活動圖片
    def close_events(self):
        img_path = 'img/game/001_upcoming_events.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('close events now...')
        else:
            print('error in close events')

    # 點封面圖
    def click_logo(self):
        img_path = 'img/game/version_logo.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('click logo now...')
        else:
            print('error in click logo')

    # 點封面圖
    def choose_world(self):
        img_path = 'img/game/choose_world.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('choose world now...')
        else:
            print('error in choose world')

    # 選角開始遊戲
    def start_game(self):
        img_path = 'img/game/start_game.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('start game now...')
        else:
            print('error in start game')

    # 自動戰鬥結果確認
    def auto_fight_result(self):
        img_path = 'img/game/auto_fight_result.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('auto fight result now...')
        else:
            print('error in auto fight result')

    # 自動戰鬥
    def auto_fight(self):
        img_path = 'img/game/auto_fight.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('auto fight now...')
        else:
            print('error in auto fight')

    # 自動戰鬥
    def auto_fight_use(self):
        img_path = 'img/game/auto_fight_use.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('auto fight use now...')
        else:
            print('error in auto fight use')

    # 自動戰鬥
    def auto_fight_start(self):
        img_path = 'img/game/auto_fight_start.png'
        res = self.move_img_and_click(img_path)

        if res == 1:
            print('auto fight start now...')
        else:
            print('error in auto fight start')

    # 移至指定圖片並點擊
    def move_img_and_click(self, img_path, duration=1):
        img_location = pyautogui.locateOnScreen(image=img_path)
        if img_location:
            x, y = pyautogui.center(img_location)
            pyautogui.moveTo(x, y, duration=duration)
            pyautogui.click()
            return 1
        else:
            return 0

    # 等待
    def standby(self, second = 5):
        print(f'waiting {second} seconds')
        time.sleep(second)
        print(f'waiting finished')

    # 滑鼠當前座標
    def mouse_posotion(self):
        while True:
            x, y = pyautogui.position()
            print(x, y)
    # mouse_posotion()

    # 登入頁面

    def loop_window_show(self, second, window):
        is_window_show = False
        while is_window_show == False:
            is_window_show = self.is_window_on_screentop(window)
            if is_window_show == False:
                self.standby(second)

    def is_window_on_screentop(self, window):
        try:
            # 获取指定标题的窗口
            window = pygetwindow.getWindowsWithTitle(window)[0]

            # 获取屏幕的宽度和高度
            screen_width, screen_height = pyautogui.size()

            # 检查窗口的位置是否在屏幕范围内
            if 0 <= window.left <= screen_width and 0 <= window.top <= screen_height:
                print(f"找到标题为 '{window}' 的窗口。")
                return True
            else:
                print(f"找不到标题为 '{window}' 的窗口。")
                return False
        except IndexError:
            print(f"找不到标题为 '{window}' 的窗口。")
            return False

