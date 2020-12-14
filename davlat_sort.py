# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:26:22 2020

@author: Shohzod
"""

#python izohli lug'

# python={
# "boolean":'mantiqiy qiymat',
# "if":"shart operatori",
# "for":"biron amalni qayta bajarish tsikli",
# "integer":"butun son",
# "float":"haqiqiy son",
# "list":"royhat",
# "set":"bir hil qiymatga egalarini chiqarmaydi",
# "dic":"lugat"
# }

# for i in python:

#     print(f"{i.title()} - {python[i].capitalize()}")

# davlat va poytaxtlar
davlatlar={
"Uzbakiston":"toshkent",
"aqsh":"vashington",
"rossiya":"moskva",
"italiya":"rim",
"fransiya":'parish',
"Yunoniston":"afina",
"Avstriya":"vena"
}

davlatlar = {k.upper():v.upper() for k,v in davlatlar.items()}

for davlat in sorted(davlatlar.keys()):
    print(f"{davlat.title()} - {davlatlar[davlat].capitalize()}")

    









