# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
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
def cmd_print():
    print('Show in command window...')
    return
def cmd_pop():
    tk.messagebox.showinfo(title='Information',
                           message='Mouse clicked !')
    tk.messagebox.showwarning(title='Warning',message='Warning Information')
    tk.messagebox.showerror(title='Error', message='Error Information')

    print('Show in commnd window...')
    return

# btn_help = tk.Button(top_win, text='Push me!', command=cmd_pop)
# btn_help.pack()
# ---------------------------------
button_relieves = ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken')
for r in button_relieves:
    tk.Button(top_win, text=r, relief=r, width=10, height=2).pack()

image = Image.open('mybk2.jpg')
bk_img = ImageTk.PhotoImage(image)
btn_try_pic = tk.Button(top_win, text='try pic', compound='center', image=bk_img)
btn_try_pic.pack()


# show window and get into event loop
top_win.mainloop()
