# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:18:39 2020

@author: User
"""


import  pygal

line_chart=pygal.Line()
line_chart.x_labels=["Yanvar","Fevral","Mart","Aprel"]
line_chart.title="Statistika"
Facebook=input("facebokk uychun 3 t qiymat kiritng\n>>>")
f=Facebook.split()
for k in range(0,len(f)):
    f[k]=int(f[k])



line_chart.add("Facebook",f)
line_chart.add("Telegram",[2.1,4.6,5.4])
line_chart.render_in_browser()



