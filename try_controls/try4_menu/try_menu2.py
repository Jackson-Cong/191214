# -*- coding: UTF-8 -*-
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root Window
win_size_pos = '800x600'

# win_size_pos = '360 x 60'
top_win.geometry(win_size_pos)

# ---------------------------------
def cmd_undo():
    tk.messagebox.showinfo(title='Info', message='Undo')
    return

def cmd_redo():
    tk.messagebox.showinfo(title='Info', message='Redo')
    return

menubar = tk.Menu(top_win)
menubar.add_command(label='Undo', command=cmd_undo)
menubar.add_command(label='Redo', command=cmd_redo)

frame= tk.Frame(top_win, width=400, height=400,bg='#7A95A7')
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)
frame.bind('<Button-3>', popup)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
