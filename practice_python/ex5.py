#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Take two lists, say for example these two:
# and write a program that returns a list that contains only the elements that are common between the lists (
# without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point -
# we’ll get to it # soon)

import random

def arraycross():

    a = [1,2,3,4,5,6,7,8,9,10] 
    b = [1,33,3,43,5,63,7,83,9,103]

    random.shuffle(a)
    random.shuffle(b)

    c = []

    for i in a:
        for j in b:
            if j == i: 

                c.append(j)


    c.sort()
    print(c)




arraycross()
