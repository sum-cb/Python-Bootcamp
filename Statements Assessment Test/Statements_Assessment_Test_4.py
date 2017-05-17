# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:15:45 2017

@author: sum_c
"""

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

lst = st.split(' ')
for word in lst:
    if len(word) % 2 == 0:
        print word + ": even"
    else :
        print word + ": not even"
        