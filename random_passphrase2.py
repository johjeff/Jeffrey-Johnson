# -*- coding: utf-8 -*-
"""
Diceware Passphrase Generator

Takes number of words for passphrase length as an argument
"""
#%%
import secrets
import sys 

def indexnum():
    """
    Create a number composed of 5 random integers between 1 and 6
    to simulate rolling 5 dice. Represents a word in a Diceware
    Dictionary
    """
    ranword = ""
    for ct in range(0,5):
    #print(secrets.choice([1,2,3,4,5,6]),end="")
    #ranword.append(secrets.choice([1,2,3,4,5,6]))
        ranword += str(secrets.choice([1,2,3,4,5,6]))
    return(ranword)

def dictionary(index):
    """
    Find the number created by indexnum() in the Diceware
    password list and return it to passphrase()
    """
        #if 'ranword' in open('./beale.wordlist.asc').read():
            #lines = ranword.readlines()
            #print(lines)
    with open("./beale.wordlist.asc") as list:
        for line in list:
            for part in line.partition(' '):
                if index in part:
                    wd1,wd2 = line.split(None,1)
                    return(str(wd2))

def passphrase():
    """
    Main program to create a random Diceware passphrase. 
    Specify number of words desired. Calls indexnum to 
    create a 5 digit number. Calls dictionary() to lookup
    the 5 digit numbers and return associated word.
    """
    passwd = ""
    words = int(input("How many words do you want? "))
    if words < 1:
        sys.exit("You entered a value less than 1. You must enter a positive integer!")
    
    #elif isinstance(words,float) == 'True':
        #sys.exit("You entered a float. You must enter a positive integer!")
        
    print(" ")
    while words >= 1:
        index = indexnum()        
        passwd += str(dictionary(index))
        words = words - 1
    print(passwd,end='')
        
passphrase()