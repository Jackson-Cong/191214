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
# 准备下拉框内的数据
data_province = ('安徽省', '江苏省', '浙江省')
city_AH = ('合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市',
           '黄山市', '滁州市', '阜阳市', '宿州市', '巢湖市', '六安市', '亳州市', '池州市', '宣城市')
city_JS = ('南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市',
           '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市')
city_ZJ = ('杭州市', '宁波市', '温州市', '嘉兴市', '湖州市',
           '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市')
data_cities = (city_AH, city_JS, city_ZJ)

def func_combo1_selected(event):
    '主从 combo 联动函数'
    sn = combo_province.current()
    # print(sn)
    combo_city['values'] = data_cities[sn]
    combo_city.current(0)
    refresh_lbl()
    return

def func_combo2_selected(event):
    '把所选择的省市信息放在 label 里显示'
    p = combo_province.get()
    c = combo_city.get()
    lbl_info['text'] = 'Address is %s %s' % (p,c)
    return

combo_province = ttk.Combobox(top_win, width=20, state='readonly', values=data_province)
# combo_province['value'] = data_province
combo_province.place(x=40,y=40)
combo_province.current(0)
combo_province.bind('<<ComboboxSelected>>', func_combo1_selected)
# city_AH 是[0]

combo_city = ttk.Combobox(top_win, width=20, state='readonly')
combo_city['values'] = data_cities[0]
combo_city.place(x=220,y=40)
combo_city.current(0)
combo_city.bind('<<ComboboxSelected>>', func_combo2_selected)

lbl_info = tk.Label(top_win,
                    width=200,
                    height=20,
                    anchor='nw',
                    text='请选择省市...')
lbl_info.place(x=40, y=80)
# ---------------------------------

# show window and get into event loop
top_win.mainloop()
