# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:20:07 2020
List bilan ishlash
@author: Shohzod
"""
persons=("abdusamatov shohzod","abdullayev javohir","abdualimov abduaziz",
         "abdualimov feruz","norbotayev sharof","aliyev javohir","begimov begzod")

sonlar=[1,2,1,5,487,5,42,45,23,56,2,5,6,52,56,2699,69,6,699,5]

#sonlar2=sonlar[:] nusxa olindi
#sonlar2.append(7)
#print(sonlar)
#print(sonlar2)
#print(sonlar[3:6])
my_friend=persons[2:5]
persons=list(persons)
persons.append("yangi")
persons=tuple(persons)
print(persons)
