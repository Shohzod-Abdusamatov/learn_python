# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:25:46 2020

@author: Shohzod
"""

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
}

for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['familiya'].title()} "
          f"{info['tyil']} da tugilgan "
          f"Malumoti {info['malumot']}:\n"
          f"Biladigan tillari:"
        )
    for til in info["tillar"]:
        print(til.upper())