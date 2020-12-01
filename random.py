# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:33:10 2020

@author: Shohzod

"""
from random import randint



for i in range(0,5):
    a=randint(1, 500)
    b=randint(1, 500)
    c=int(input("{}+{}=".format(a,b)))

    if(a+b==c):
        print("TO'G'RI")
    else:
        print("XATO")






