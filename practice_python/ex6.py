#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Ask the user for a string and print out whether this string is a palindrome or not.

def reverse(word):
    x = ''

    i = 0
    while(i < len(word)):
        x += word[len(word) -1 - i]

        i+=1
    return x


word = raw_input()

wordr = reverse(word)

if word == wordr:
    print("palindrome!")
else:
    print("nah")
