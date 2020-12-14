# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:23:32 2020

@author: User
"""

menu={
"osh":5200,
"manti":1520,
"tuxum":200,
"lagmon":520,
"tabaka":5245,
"jiz":7854,
"shashlik":2451,
"non":1452,
"sho'rva":1452,
"somsa":1452
}

#menu={k.lower() for k in menu}

n=int(input("Nechta buyurtma bermoqchisiz\n>>"))
buyurtma=[]
print(menu)
for i in range(0,n):
    buyurtma.append(input(f"{i+1} - taom:  "))

print(buyurtma)
for taom in buyurtma:
    if taom in menu :
        print(taom ,menu[taom], " so'm")

for taom in buyurtma:
    if taom not in menu :
        print(taom + " yo'q")