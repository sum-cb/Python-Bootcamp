# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:26:06 2017

@author: sum_c
"""

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

list = [char[0] for char in st.split(" ") ]
print list