# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:39:47 2019

@author: Florian
"""
import os

# list the names from Keyword.txt
def list():
    with open("Keyword.txt", "r") as input:
        for line in input:
            stripped = line.rstrip('\n')
            print(stripped)
    
# add new name to the Keyword.txt file
def add(name):
    with open("Keyword.txt", "r+") as file:
        for line in file:
            if name in line:
               print(f"{name} is already in the list. Not adding it.")
               break
        else: # not found, we are at the eof, apped the new name
            file.write("\n" + name)
            print(f"{name} appended to the list")

# remove name from the Keyword.txt file
def remove(name):
    with open("Keyword.txt", "r") as input:
        with open("temp.txt", "w") as output: 
            for line in input:
                if line.strip("\n") != name:
                    output.write(line)
    os.replace("temp.txt", "Keyword.txt")
