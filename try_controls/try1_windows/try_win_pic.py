# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root Window
win_size_pos = '800x600'

# win_size_pos = '360 x 60'
top_win.geometry(win_size_pos)

# ---------------------------------
image = Image.open('图片2_副本.png')
bk_img = ImageTk.PhotoImage(image)

lbl_background = tk.Label(
        top_win, text='Hello World', bg='black', image=bk_img)
lbl_background.place(x=0, y=0, width=800, height=600)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
