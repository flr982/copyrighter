# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:52:05 2019

@author: Florian
"""
# make a list of names that should have the ® symbol appended
brands = open("Keyword.txt",'r').read().split('\n')

# append ® to each name included in the Keyword.txt file
def main(text):
    for name in brands:
        text = text.replace( name, name + '\xae')
    print(f"The modified text is: {text}")
