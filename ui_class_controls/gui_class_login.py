# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class UC_Login:
    def __init__(self, pwin):
        print('UC_Login class created !')
        self.parent_win = pwin

        self.parent_win.title('Login - By Class')
        win_size_pos = '300x200'
        self.parent_win.geometry(win_size_pos)

        #对本窗体进行自动布局
        self.init_widgets()
        return

    def init_widgets(self):
        '对本窗体进行布局'
        lbl_info = tk.Label(
            self.parent_win,
            text='Login form',
            anchor='w',
            justify='left',
            bg='purple',
            fg='white',
            height=1
        )

        lbl_info.place(x=20, y=20, width=260)


        default_var = tk.StringVar(value='Hello Jackson')
        self.ent_username = tk.Entry(
            self.parent_win,
            show=None,
            textvariable=default_var,
        )
        self.ent_username.place(x=20, y=60)


        default_var = tk.StringVar(value='Password')
        self.ent_password = tk.Entry(
            self.parent_win,
            show='*',
            textvariable=default_var,
        )
        self.ent_password.place(x=20, y=100, width=260)

        self.btn_login = tk.Button(
            self.parent_win,
            text='Sign in',
            relief='raised',
            width=10, height=2,
            bg='#ceceff', fg='white',
            command = self.__cmd_login,
            )
        self.btn_login.place(x=20, y=140, width=50)

        lbl_info = tk.Label(
            self.parent_win,
            text='Lost Your Password?',
            bg='white',
            fg='grey',
            width=20,
            height=1
        )
        lbl_info.place(x=140, y=160)
        return



    def __cmd_login(self):
        print(self.ent_username.get())
        print(self.ent_password.get())
        u = self.ent_username.get()
        p = self.ent_password.get()

        if u == 'admin' and p =='666':
            tk.messagebox.showinfo(title='Information', message='Succeed!')
            self.login_status = 'OK'
            self.parent_win.quit()
        else:
            tk.messagebox.showerror(title='Information', message='Wrong user name or password')
            self.login_status = 'No'
        return
