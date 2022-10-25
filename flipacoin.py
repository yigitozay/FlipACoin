# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 07:04:09 2022

@author: mgtfi
"""

import random

def tosscoinA():
    if random.uniform(0, 1) <=0.11:
        return "tails"
    else:
        return "heads"
    
def tosscoinB():
    if random.uniform(0, 1) <= 0.79:
        return "tails"
    else:
        return"heads"
        

print("With how much money do you want to play?")
total_money =int(input())
print("How many times do you want to play?")
nb_flips = int(input())

for i in range(nb_flips):
    if total_money % 4 == 0:#checking if the total money is a multiple of four or not
        coin = tosscoinA()
    else:
        coin = tosscoinB()
    
    if coin == "tails":
        total_money +=1 # earn 1 dollar if you get tails
    else:
        total_money-=1 #lose 1 dollar otherwise
        
print("After", nb_flips, "flips, you have $", total_money, "of total money")