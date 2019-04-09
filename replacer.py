# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:52:05 2019

@author: Florian
"""
import os

# make a list of names that should have the ® symbol appended
brands = open("static/Keyword.txt",'r').read().split('\n')

# append ® to each name included in the Keyword.txt file
def rpl(text):
    for name in brands:
        text = text.replace( name, name + '\u00ae')
    os.remove("output.txt")
    f = open("output.txt","w+")
    f.write(text)
    f.close()
    return "OK \n"

    #text = text + '\n'
    #return text

