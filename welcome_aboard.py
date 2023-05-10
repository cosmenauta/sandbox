#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:18:36 2023

@author: cosmemirallescarol
"""


if __name__ == "__main__":

    a = input("What's your name: ")
    print("Welcome aboard:", a)
    
    from hello_world import hello_world
    
    print("Now all together:", hello_world())
    
    from hipotenuse import hipotenuse
    
    print("Let's calculate the length of a rectangle triangle.")
    x = int(input("Give one length: "))
    y = int(input("Give another length: "))
    print("The length of the hipotenuse is: ", hipotenuse(x,y))
        
