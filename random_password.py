# -*- coding: utf-8 -*-
"""
Random Password Generator

Takes password length as an argument
"""

import random
import string

def password():
    length = int(input("How many characters do you want? "))
    while length >= 1:
        char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        print(char,end="")
        length = length - 1
        
password()