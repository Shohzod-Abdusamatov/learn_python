# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:20:58 2020

@author: Shohzod
"""
#name=input("what is your name?\n>>>")

    #print("Salom {}".format(name))
#print("{:.5}".format(name))

#print(name[::-1].capitalize()) teskari tartibda chiqaradi
name="shohzod abdusamatov"
name=name.title()
print(name)


a=name.split()[0] #split massivga ajratadi
b=name.split()[1]
name=b+" "+a
print(name)


