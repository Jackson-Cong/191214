# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root Window
win_size_pos = '800x600'

# win_size_pos = '360 x 60'
top_win.geometry(win_size_pos)

# ---------------------------------
# step1: Create frame
frame_root1 = tk.Frame(top_win, bg='#74596E', width=760, height=200)

frame_root1.place(x=20, y=20)

var_sel = tk.IntVar()
var_sel.set(0)

def show_selected():
    print(var_sel.get())
    return

radio_btn1 = tk.Radiobutton(frame_root1,
                            text='one',
                            value=0,
                            variable=var_sel,
                            bg='blue',
                            fg='white',
                            command=show_selected)
radio_btn1.place(x=20, y=20)

radio_btn2 = tk.Radiobutton(frame_root1,
                            text='two',
                            value=1,
                            variable=var_sel,
                            bg='blue',
                            fg='white',
                            command=show_selected)
radio_btn2.place(x=70, y=20)

radio_btn3 = tk.Radiobutton(frame_root1,
                            text='three',
                            value=2,
                            variable=var_sel,
                            bg='blue',
                            fg='white',
                            command=show_selected)
radio_btn3.place(x=115, y=20)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
