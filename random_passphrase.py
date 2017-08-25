# -*- coding: utf-8 -*-
"""
Password Generator

Takes number of words for passphrase length as an argument
"""

import secrets
import linecache

def passphrase():
    words = int(input("How many words do you want? "))
    while words >= 1:
        ranword = ""
        for ct in range(0,5):
            print(secrets.choice([1,2,3,4,5,6]),end="")
            ranword.append(secrets.choice([1,2,3,4,5,6]))
            #ranword += str(secrets.choice([1,2,3,4,5,6]))
        print(" ")
        if 'ranword' in open('./beale.wordlist.asc').read():
            lines = ranword.readlines()
            print(lines)
        print(ranword,end="\n")
        #with open("./beale.wordlist.asc") as list:
            #for line in list:
                #for part in line.partition(' '):
                    #if ranword in part:
                        #wd1,wd2 = line.split(None,1)
                        #print(wd2)
        words = words - 1
        
passphrase()