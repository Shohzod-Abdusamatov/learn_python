# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:23:21 2020

@author: Shohzod
"""
#set, list, lug'at
mahsulotlar={
"olma":1500,
"olma":1501,
"uzum":2100,
"banan":1522,
"nok":2100,
}
bozorlik=["olma","uzum","anjir","non"]


for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} ning narhi {mahsulotlar[mahsulot]}")

for mahsulot in bozorlik:
    if mahsulot not in mahsulotlar:
        print(f"Iltimos {mahsulot.title()}  ham olib keling!")

talabalar={"Shohzod","Sardor","Siroj","Shohzod","Anvar","Aziz","Sardor"}
print(talabalar)
print(sorted(set(mahsulotlar.keys())))