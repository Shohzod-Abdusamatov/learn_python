# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:59:40 2020

@author: Shohzod
"""
import math

#print(math.ceil(8.3)) #kattaga yahlitlaydi
#print(math.floor(8.7)) #kichikka yahlitlaydi
#print(math.sqrt(3))

son=int(input("sonni kiritng: "))

print("kiritilgan son:{}".format(son))   #687

ikki=son%100
bir=ikki%10
on=ikki//10
yuz=son//100

print(yuz+on+bir)



