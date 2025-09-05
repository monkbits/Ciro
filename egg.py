import os
import modules.define as define
import pyautogui
import math
import time
import ctypes
from modules.actions import Action

a = Action() 
# a.printpos()
# a.write_mail("task update",define.a)
# a.make_circle()
# a.lock_pc()

# import tkinter as tk
# import pyautogui

# def update_mouse_pos():
#     x, y = pyautogui.position()
#     label.config(text=f"Mouse Position: {x}px, {y}px", font=("Helvetica", 20), bg='lightblue', fg='darkblue')
#     label.pack(pady=20)
#     root.after(100, update_mouse_pos)  # update every 100ms

# root = tk.Tk()
# root.title("Pixel Position Widget")

# label = tk.Label(root, font=("Arial", 20))
# label.pack(padx=20, pady=20)

# update_mouse_pos()  # start updating mouse position

# root.mainloop()


from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QButtonGroup, QPushButton, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import sys
import pprint
from  modules.mouseloc import showmospos

# pprint.pprint(dir(QTextEdit))
# exit()

app = QApplication(sys.argv)

x, y = pyautogui.position()
window = QWidget()
window.setWindowIcon(QIcon('eggicon.png'))
window.setWindowTitle("Egg | notes app")
window.setStyleSheet("background-color: #1b2021")  # sky blue background

def getButton(text="save", style="color: white;padding-bottom: 10px 0px;font-size:15px; background-color: #2b4452"):
        btn = QPushButton(text);
        btn.setStyleSheet(style);
        if text == "Actions":
            def changepage():
                # create new layout
                new_layout = QHBoxLayout()
                
                # create label
                lbl = QLabel("normal")
                new_layout.addWidget(lbl)
                
                # ⚠️ replace old layout with new one
                QWidget().setLayout(window.layout())  # disconnect old layout
                window.setLayout(new_layout)

            btn.clicked.connect(changepage)

        return btn

savebtn = getButton("save");
cancelbutton = getButton("Cancel");


message = QLabel("")
message.setStyleSheet("color: white; font-size: 16px")

def load_text(text_area, filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            text_area.setPlainText(content)
    else:
        text_area.setPlainText("No saved file found.")

def save_text():
    text = text_area.toPlainText()
    with open("savedtext.txt", "w", encoding="utf-8") as f:
            f.write(text)
    message.setText("saved!")
    QTimer.singleShot(2000, lambda: message.setText(""))
    

def get_select_box():   
    combo = QComboBox();
    combo.setStyleSheet("""
        QComboBox {
            color: white;
            background-color: #444;
            border: 1px solid #888;
            padding: 5px;
            height: 26px;
            font-size: 20px;
        }
                        
        QComboBox QAbstractItemView {
            margin: 4px;             
            padding-left: 10px;      
            height: 30px!important;
            background-color: #222;
            color: white;
            selection-background-color: #494a5c;
            selection-color: #fff;
        }
                        
        QComboBox QAbstractItemView::item {
            margin: 4px;             
            padding-left: 10px;    
            height: 30px;           
        }

        QComboBox::drop-down {
            height: 100px;
            padding: 5px;
            border: 0px;
        }

        

        QListView {
            background-color: #222;
            color: white;
            selection-background-color: #494a5c;
            selection-color: black;
            padding: 5px;
            show-decoration-selected: 1;
        }

        QListView::item {
            padding: 10px;         
            margin: 4px;
            height: 30px;
        }
    
    """)
    combo.setMaximumWidth(200)
    combo.addItem("Option 1")
    combo.addItem("Option 2")
    combo.addItem("Option 3")
    label = QLabel("Selected: ")
    def on_selection_changed():
        selected = combo.currentText()
        label.setText(f"Selected: {selected}")

    combo.currentIndexChanged.connect(on_selection_changed)
    return combo , label;


combo , label3 = get_select_box();


savebtn.clicked.connect(save_text)

bg = QButtonGroup();
bg.addButton(savebtn);
bg.addButton(cancelbutton);


# Text area widget
text_area = QTextEdit()
text_area.setStyleSheet("color: white; font-size: 18px")
text_area.setPlaceholderText("Enter your text here...")
text_area.setFixedSize(400,200)

load_text(text_area,"savedtext.txt");

line2 = QHBoxLayout()
line2.addWidget(savebtn)
line2.addWidget(cancelbutton)

layout = QVBoxLayout()

label = QLabel("Mouse position: (0, 0)")
label.setStyleSheet("color: white; font-size: 12px; font-weight: bold;padding: 30px 0")


def get_menu():
    h_layout = QHBoxLayout()
    h_layout.addWidget(getButton("Home"))
    h_layout.addWidget(getButton("Actions"))
    h_layout.addWidget(getButton("Notes"))
    h_layout.addWidget(getButton("Help"))
    return h_layout



def add_field(layout):
    f = QLineEdit() 
    f.setPlaceholderText("x postion")
    f.setStyleSheet("color: white;width: 50px; font-size: 14px;padding: 8px 4px")
    layout.addWidget(f)

def make_form():
    h_layout = QHBoxLayout()
    add_field(h_layout)
    add_field(h_layout)
    add_field(h_layout)
    layout.addLayout(h_layout) 



def compile_layout():
    layout.addLayout(get_menu())
    layout.addWidget(message)
    layout.addWidget(combo)
    layout.addWidget(label3)
    layout.addWidget(text_area)
    layout.addLayout(line2)
    make_form()
    layout.addWidget(label)
    window.setLayout(layout)
    print()

compile_layout()


timer = showmospos(label)


window.show()
sys.exit(app.exec_())





