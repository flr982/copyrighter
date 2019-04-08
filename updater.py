# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:39:47 2019

@author: Florian
"""
import os

# list the names from Keyword.txt
def list():
    keyword_list = []
    with open("static/Keyword.txt", "r") as input:
        for line in input:
            stripped = line.rstrip('\n')
            keyword_list.append(stripped)
    return keyword_list
    
# add new name to the Keyword.txt file
def add_key(name):
    with open("static/Keyword.txt", "r+") as file:
        for line in file:
            if name in line:
               return (f"{name} is already in the list. Not adding it.")
               break
        else: # not found, we are at the eof, apped the new name
            file.write("\n" + name)
            print(f"{name} appended to the list")
            return "Done"

# remove name from the Keyword.txt file
def rm_key(name):
    with open("static/Keyword.txt", "r") as input:
        with open("static/temp.txt", "w") as output: 
            for line in input:
                if line.strip("\n") != name:
                    output.write(line)
    os.replace("static/temp.txt", "static/Keyword.txt")
    return "Done"
