# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:12:39 2020

@author: abdelhak kelious
"""
from random import randint


def monty_hall(change):
    doors=["door1","door2","door3"]
    choice=randint(0,2)
    reward=randint(0,2)
    open_door=None

    if change:
        while True :
            open_door=randint(0,2)
            if open_door!=choice and open_door!= reward: 
                break
        for i in doors:
            if doors.index(i)!= open_door and doors.index(i)!=choice:
                choice=doors.index(i)

    if choice==reward:
        return 1
    else :
        return 0


def monty_hall_simulation(n):
    x=0
    for i in range(n):
        x+=monty_hall(True)

    y=0
    for i in range(n):
        y+=monty_hall(False)
    return (x/n,y/n)


print(monty_hall_simulation(1000000))
