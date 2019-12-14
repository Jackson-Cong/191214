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

text_of_btn = ('北京', '上海', '广州', '深圳')
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
value_of_btn = (v1, v2, v3, v4)

'''
chk_btn1 = tk.Checkbutton(frame_root1,
                          text=text_of_btn[0],
                          variable=value_of_btn[0],
                          command=None
                          )
chk_btn1.place(x=20, y=40)
'''

def show_selected():
    print('---')
    for v in value_of_btn:
        print(v.get())
    return

for idx in range(4):
    chk_btn = tk.Checkbutton(frame_root1,
                              text=text_of_btn[idx],
                              variable=value_of_btn[idx],
                              command=show_selected
                              )
    chk_btn.place(x=20 + idx*100, y=40)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
