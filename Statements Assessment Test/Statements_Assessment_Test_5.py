# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:21:48 2017

@author: sum_c
"""

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".

for number in range(1,100):
    if (number % 3 == 0) and (number % 5 ==0):
        print "FizzBuzz"
    elif (number % 5 == 0):
        print "Fizz"
    elif (number % 3 == 0):
        print "Buzz"
    else:
        print number