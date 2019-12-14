# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root Window
win_size_pos = '300x250'

# win_size_pos = '360 x 60'
top_win.geometry(win_size_pos)

# ---------------------------------
# step 1
lbl_info = tk.Label(
    top_win,
    text='Login form',
    anchor='w',
    justify='left',
    bg='purple',
    fg='white',
    width=35,
    height=1
)

lbl_info.place(x=20, y=20)

default_var = tk.StringVar(value='Username')
entry_cleartext = tk.Entry(
    top_win,
    show=None,
    bg='white',
    width=23,
    textvariable=default_var,
    font=('Arial', 14)
)
entry_cleartext.place(x=20, y=60)

def cmd_check():
    u = ety_username.get()
    print(u)
    p = ety_password.get()
    print(p)
    if u!='123456':
        tk.messagebox.showinfo(title='Information',
                                message='Username is wrong')
    elif p!='123456':
        tk.messagebox.showinfo(title='Information',
                                message='Password is wrong')
    else:
        tk.messagebox.showinfo(title='Information',
                                message='Well done')
    return


default_var = tk.StringVar(value='Password')
entry_cleartext = tk.Entry(
    top_win,
    show=None,
    bg='white',
    textvariable=default_var,
    width=23,
    font=('Arial', 14)
)
entry_cleartext.place(x=20, y=100)
entry_cleartext.get()


btn_text = tk.Button(top_win, text='Log in', bg='purple',
                     fg='white', relief='raised', width=13, height=3)
btn_text.place(x=20, y=140)

lbl_info = tk.Label(
    top_win,
    text='Lost Your Password?',
    bg='white',
    fg='grey',
    width=20,
    height=1
)
lbl_info.place(x=140, y=160)


# ---------------------------------

# show window and get into event loop
top_win.mainloop()
