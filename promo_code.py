# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:44:59 2020

@author: Shohzod
"""
from random import randint
myList=[132,135,136]

myNumber=randint(130, 140)

i=0
while myNumber in myList:
    myNumber=randint(130, 140)
    i+=1
print("TAKRORLANISH SONI:",i)
print(myNumber)