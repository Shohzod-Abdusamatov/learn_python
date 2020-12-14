# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:02:22 2020

@author: Shohzod
"""

# masala
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlatlar={
"Uzbekiston":"toshkent",
"aqsh":"vashington",
"rossiya":"moskva",
"italiya":"rim",
"fransiya":'parish',
"Yunoniston":"afina",
"Avstriya":"vena"
}

davlat=input("davlatni kirirting?\n>>")
davlatlar = {k.capitalize():v.capitalize() for k,v in davlatlar.items()}
davlat=davlat.capitalize()
#print(davlatlar.get(davlat.capitalize(),"BUNDAY DAVLAT ROYHATDA YO'Q"))
if(davlat.capitalize() in davlatlar.keys()):
    print(f"{davlat}ning poytaxti {davlatlar[davlat]} shahri")
else:
    print("bunday davlat royhatda yoq")

