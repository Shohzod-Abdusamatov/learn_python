# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:50:44 2020

@author: Shohzod
"""
#numbers=list(range(1,11))

#for number in numbers:
#    print(number,"\tning kvadrati",number**2)
#xabar=" yaxshimisan nima gapla"
#ism=["Shohzod","Sardor","Sanjar","Sirpoj","Alisher"]
##   print(i+xabar)
#print("kod",len(ism),"marta takrorlandi")

#sonlar=list(range(11,100,2))

#for son in sonlar:
#   print(son**3)

#kinolar=[]
#for i in range(5):
#    kino=input("sevimli kinoni kiriitng\n>>>")
#    kinolar.append(kino)
#print(kinolar)

kinolar=[]
n=int(input("nechta kino kerak\n>>"))
for i in range(n):
    kinolar.append(input(f"{i+1}-chi kinoni kiritng >> "))
print(kinolar)