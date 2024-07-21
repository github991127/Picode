# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:17:26 2021

@author: Administrator
"""

from KMP import Solution

def return_bir(birthday):    
    filename = '改写一亿.txt'
    with open(filename) as file_object:
        contents = file_object.read()
    
    if birthday in contents:
        a = Solution()
        return (a.kmp(contents,birthday))
    else:
        return (0)
    