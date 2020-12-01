# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:00:52 2020

@author: Shohzod
"""
son=input("1 dan 30 gacaha sonlarni kiriting!\n>>>")#24

if son.isdigit():
    son=int(son)
    if son>0 and son<100:
        qoldiq=son%10
        butun=son//10
        letter=""
        if butun==1:
            letter+="o'n"
        elif butun==2:
            letter+="yigirma"
        elif butun==3:
            letter+="o'ttiz"
        elif butun==4:
            letter+="qirq"
        elif butun==5:
            letter+="elliik"
        elif butun==6:
            letter+="oltmish"
        elif butun==7:
            letter+="yetmish"
        elif butun==8:
            letter+="sakson"
        elif butun==9:
            letter+="to'qson"
            #birlik
        if qoldiq==1:
            letter+="bir"
        elif qoldiq==2:
            letter+="ikki"
        elif qoldiq==3:
            letter+="uch"
        elif qoldiq==4:
            letter+="to'rt"
        elif qoldiq==5:
            letter+="besh"
        elif qoldiq==6:
            letter+="olti"
        elif qoldiq==7:
            letter+="yetti"
        elif qoldiq==8:
            letter+="sakkiz"
        elif qoldiq==9:
            letter+="to'qqiz"
    else:
        print("qiymat notogri kiritildi")
else:
    print("Son kiritng")
print(letter)





