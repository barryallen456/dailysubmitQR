from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
from time import sleep
import win32con

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
id=0
for h, t in hwnd_title.items():
     if t != "":
         print(h, t)
         if t == "粤省事":

             id = h

sleep(3)
hwnd = id
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 强行显示界面后才好截图
win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
sleep(1)
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")