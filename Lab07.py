# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:42:22 2017

@author: piccini5
"""

from operator import itemgetter

open_file = open("scores.txt","r")

surname_list = []
scores_list = []
scores_tup = []

for line in open_file:
    
    split_line = line.split()
    
    if split_line == []:
        continue
    
    last,first = line.split(",")
    surname_list.append(last)
    
    last = split_line[0]
    
    scores_list = split_line[2:4]
    average = (int(scores_list[0]) + int(scores_list[1])) / 2.0
                   
    split_line.append(average)
    
    values = tuple(split_line)
    scores_tup.append(values)
    
sorted_alpha = sorted(scores_tup, key = itemgetter(0))

exam1_scores = []
exam2_scores = []

print()
for item in sorted_alpha:
    sorted_list = list(item)
    exam1_scores.append(int(sorted_list[2]))
    exam2_scores.append(int(sorted_list[3]))
    print("{:12}{:10}{:5}{:5}{:5}".format(item[0],item[1],item[2],item[3],item[4]))
    
total_1 = 0
total_2 = 0
    
for item in exam1_scores:
    total_1 += item
for item in exam2_scores:
    total_2 += item  
    
exam1_average = total_1 / 5
exam2_average = total_2 / 5

print()
print(exam1_average)
print(exam2_average)  
 
open_file.close()

print("{:10}{:15}{:10}{:10}{:15}{:15}{:15}{:15}".format(item[0],\
          item[1],item[2],\
          item[3],item[4],item[5],item[6],item[7]))








