# -*- coding: utf-8 -*-
"""
Created on Wed May 17 07:50:10 2017

@author: sum_c
"""

# Use for, split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
print st

lst = st.split(" ")
print lst

for word in lst:
    if word[0] == 's':
        print word
    