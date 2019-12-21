# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

from gui_class_login import UC_Login
from gui_class_show import UC_Show

root = tk.Tk()
form_login = UC_Login(root)
root.mainloop()
root.destroy()

root = tk.Tk()
form_show = UC_Show(root)
root.mainloop()
