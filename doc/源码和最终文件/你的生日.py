# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:17:26 2021

@author: Administrator
"""

from KMP import Solution
filename = '改写一亿.txt'
with open(filename) as file_object:
    contents = file_object.read()
    
birthday = input("Enter your birthday,in the form yyyymmdd: ")
if birthday in contents:
    print("your birthday appears in the first billion digits of pi!")
    a = Solution()
    print(a.kmp(contents,birthday))
else:
    print('your birthday does not appear in the first billion of pi!')
    