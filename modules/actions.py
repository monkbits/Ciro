import pyautogui
import math
import time
import ctypes

class Action:
    def write_mail(self, mailfor, d):
        if(mailfor == "task update"):
            self.write_taskupdate_mail(d)
        elif(mailfor == "pull request"):
            self.write_pullreq_mail(d)


    def make_circle(self):
        # Settings
        radius = 100  # pixels
        center_x, center_y = pyautogui.size()
        center_x //= 2
        center_y //= 2

        # Move to start point
        start_x = center_x + radius
        start_y = center_y
        pyautogui.moveTo(start_x, start_y, duration=0.2)

        # Do one circle
        for angle in range(0, 361, 10):  # 0 to 360 degrees in steps
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            pyautogui.moveTo(x, y, duration=0.01)

        print("Mouse rotation complete.");

    def lock_pc(self):
        ctypes.windll.user32.LockWorkStation();

    def printpos(self): 
        print(pyautogui.position())
        exit()

    def write_pullreq_mail(self,d):
        print("wrote pull request mail")

    def write_taskupdate_mail(self,d):
        pyautogui.click(d["mail_wala_tab"])
        time.sleep(2)
        pyautogui.click(d["reload_button"])
        time.sleep(5)
        pyautogui.click(d["new_mail"])
        time.sleep(3)
        pyautogui.write(d["tomail"])
        time.sleep(1)
        pyautogui.click(d["randomplace"])
        time.sleep(1.5)
        pyautogui.click(d["ccplace"])
        time.sleep(1)
        pyautogui.write(d["ccmail"])
        pyautogui.click(d["randomplace"])
        time.sleep(2)
        pyautogui.click(d["subjectbox"])
        time.sleep(1)
        pyautogui.write(d["submatter"])
        time.sleep(1)
        pyautogui.click(d['randomplace'])
        time.sleep(1)
        pyautogui.click(d["mainmail"])
        time.sleep(1)
        pyautogui.write(d["mergecommand"])

