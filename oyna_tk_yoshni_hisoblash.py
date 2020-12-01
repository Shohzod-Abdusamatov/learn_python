# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:19:55 2020

@author: Shohzod
"""
from datetime import datetime
from tkinter import *

oyna=Tk()
oyna.title("yosh hisobla")
oyna.geometry('300x300')
oyna.config(bg="black")

yil=Entry()
yil.place(x=75,y=30,width=150,height=30)

natija=Label(text="Natija",bg="yellow")
natija.place(x=75,y=135,width=150,height=40)
def farq():
    yosh=datetime.today().year- int(yil.get())
    natija.config(text=yosh)
    if yosh>=18:
        natija.config(bg="pink")
    else:
        natija.config(bg="white",color="blue")
tugma=Button(text="Hisobla",bg="blue",command=farq)
tugma.place(x=75,y=75,width=150,height=30)




oyna.mainloop()