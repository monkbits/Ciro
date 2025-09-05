
import pyautogui
from PyQt5.QtCore import QTimer

def showmospos(myparam):
    def update_mouse_position():
        x, y = pyautogui.position()
        myparam.setText(f"Mouse position: ({x}, {y})")


    timer = QTimer()
    timer.timeout.connect(update_mouse_position)
    timer.start(100)  
    return timer

