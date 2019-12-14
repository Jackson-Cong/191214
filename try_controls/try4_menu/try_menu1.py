# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.messagebox
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

top_menu = tk.Menu(top_win)
# 单层菜单
'''
top_menu.add_command(label='Hello', command = None)
top_menu.add_command(label='Quit', command = top_win.quit)
'''
def cmd_menu_item():
    tk.messagebox.showinfo(title='Information', message='Menu item clicked !')
    return

filemenu = tk.Menu(top_menu, tearoff = False)
filemenu.add_command(label='Open', command=cmd_menu_item)
filemenu.add_command(label='Save', command=cmd_menu_item)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=top_win.quit)

top_menu.add_cascade(label='File', menu=filemenu)

# Create second dropdown Menu
filemenu = tk.Menu(top_menu, tearoff = False)
filemenu.add_command(label='Select All', command=cmd_menu_item)
filemenu.add_separator()
filemenu.add_command(label='Copy', command=cmd_menu_item)
filemenu.add_command(label='Cut',command=cmd_menu_item)
filemenu.add_command(label='Paste', command=cmd_menu_item)
# add dropdown menu1 to top menu
top_menu.add_cascade(label='Edit', menu = filemenu)

#show the menu
top_win.config(menu=top_menu)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
