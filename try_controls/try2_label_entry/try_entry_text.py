# -*- coding: UTF-8 -*-

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
entry_cleartext = tk.Entry(
    top_win,
    show=None,
    width=50,
    font=('Arial', 14)
)
# entry_cleartext.pack()
entry_cleartext.place(x=100, y=100)

text_description = tk.Text(top_win, height=6)
text_description.pack()


# ---------------------------------

# show window and get into event loop
top_win.mainloop()
