# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:41:19 2020

@author: Shohzod
"""
#list Dictionary

myFriends={
'solohiddin':{
    'name':"solohiddin",
    'age':21,
    'car':"BMW"
    },
'alisher':{
    'name':"alisher",
    'age':22,
    'car':"lacetti"
    },
'javohir':{
    'name':"javohir",
    'age':20,
    'cars':{
        'car1':"spark",
        'car2':"cobalt"
        }
    },
}

solohiddin=myFriends['solohiddin']
alisher=myFriends['alisher']
javohir=myFriends['javohir']

print(myFriends['javohir']['cars']['car2'])












