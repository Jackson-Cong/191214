# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class UC_Show:
    def __init__(self, pwin):
        print('UC_Show class created !')
        self.parent_win = pwin

        self.parent_win.title('Show - By Class')
        win_size_pos = '300x200'
        self.parent_win.geometry(win_size_pos)

        #对本窗体进行自动布局
        self.init_widgets()
        return

    def init_widgets(self):
        '对本窗体进行布局'
        lbl_info = tk.Label(
            self.parent_win,
            text='Show form',
            anchor='w',
            justify='left',
            bg='purple',
            fg='white',
            height=1
        )

        lbl_info.place(x=20, y=20, width=260)
        return
