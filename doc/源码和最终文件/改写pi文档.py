# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:21:39 2021

@author: Administrator
"""


filename_1 = '前一亿位.txt'
filename_2 = '改写一亿.txt'
with open(filename_1) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    line_1 = line.strip()[:55]
    pi_string += line_1.replace(' ','')
    
pi_string = '3'+pi_string

with open(filename_2,'w') as file_object:
    file_object.write(pi_string)

