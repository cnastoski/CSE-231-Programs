# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:17:34 2017

@author: welshtor
"""

#Prompt user to input value

num_chk1 = input("Please input an integer that is not 0: ")

#Convert value to integer

int1 = int(num_chk1)

sum_odd = 0
sum_even= 0
odd_count = 0
even_count = 0

while int1 != 0:
    print('\nGreat job!')
    
    if int1 < 0:
        num_chk1 = input("Please input an integer that is not 0: ")
        int1 = int(num_chk1)
        continue
   
    if int1 % 2:
        odd_count += 1
        sum_odd += int1
    else:
        even_count += 1
        sum_even += int1
    
    
    num_chk1 = input("Please input an integer that is not 0: ")
    int1 = int(num_chk1)


print('\nAmount of odd numbers: ',odd_count)
print('Amount of even numbers: ',even_count)
print('Sum of odd numbers: ',sum_odd)
print('Sum of even numbers: ',sum_even)
print('Total of positive integers: ',odd_count + even_count)