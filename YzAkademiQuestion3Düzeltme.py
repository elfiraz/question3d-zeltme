# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 13:30:04 2022

@author: asus
"""

ballEneryg=4

def hesapla(dizi,ballEnergy):
    for i in dizi:
        height=i
        

        if ballEnergy<height:
            newEnergy=ballEnergy-(height-ballEnergy)

        else:
            newEnergy=ballEnergy+(ballEnergy-height)

    print(newEnergy)


a = int (input("How many legos: "))
arr=[a]

for i in range (a):
    arr.append(int(input(">")))


hesapla(arr,ballEneryg)