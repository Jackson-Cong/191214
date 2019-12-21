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

default_var = tk.StringVar(value='Hello Jackson')
entry_cleartext = tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
)
entry_cleartext.place(x=20, y=60)


default_var = tk.StringVar(value='Password')
entry_cleartext = tk.Entry(
    top_win,
    show='*'',
    bg='white',
    textvariable=default_var,
)
entry_cleartext.place(x=20, y=100)
entry_cleartext.get()

def cmd_login():
    print(ent_username.get())
    print(ent_password.get())
    u = ent_username.get()
    p = ent_password.get()

    if u == 'admin' and p =='666':
        tk.messagebox.showinfo(title='Information', message='Succeed!')
    else:
        tk.messagebox.showerror(title='Information', message='Wrong user name or password')
    return

    btn_login = tk.Button(
        top_win,
        text='Sign in',
        relief='raised',
        width=10, height=2,
        bg='#ceceff', fg='white',
        command = self.cmd_login,
        )
        self.btn_login.place(x=20, y=140, width=50)
        return






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
