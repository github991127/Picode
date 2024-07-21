# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:31:09 2021

@author: Administrator
"""


def shuchu_1(b,c):
    if int(b)<10 and int(c)<10:
        return '010'+b+'0'+c
    if int(b)>=10 and int(c)<10:
        return '01'+b+'0'+c
    if int(b)<10 and int(c)>=10:
        return '010'+b+c
    if int(b)>=10 and int(c)>=10:
        return '01'+b+c
    
def shuchu_2(b,c):
    if int(b)<10 and int(c)<10:
        return '020'+b+'0'+c
    if int(b)>=10 and int(c)<10:
        return '02'+b+'0'+c
    if int(b)<10 and int(c)>=10:
        return '020'+b+c
    if int(b)>=10 and int(c)>=10:
        return '02'+b+c


list_1 = ['1','1','0']
bir_list = []
 

while int(list_1[1])<13:
    if list_1[1] in ['01','03','05','07','08','10','12']:
        while int(list_1[2])<31:
            list_1[2]=str(int(list_1[2])+1)
            bir_list.append(shuchu_1(list_1[1],list_1[2]))
    else:
        while int(list_1[2])<30:
            list_1[2]=str(int(list_1[2])+1)
            bir_list.append(shuchu_1(list_1[1],list_1[2]))
    list_1[1]=str(int(list_1[1])+1)
    list_1[2]='00'
    
list_2 = ['2','1','0']

while int(list_2[1])<13:
    if list_2[1] in ['01','03','05','07','08','10','12']:
        while int(list_2[2])<31:
            list_2[2]=str(int(list_2[2])+1)
            bir_list.append(shuchu_2(list_2[1],list_2[2]))
    else:
        while int(list_2[2])<30:
            list_2[2]=str(int(list_2[2])+1)
            bir_list.append(shuchu_2(list_2[1],list_2[2]))
    list_2[1]=str(int(list_2[1])+1)
    list_2[2]='00'
    
filename = '生日列表.txt'
with open(filename,'w') as file_object:
    for birlist in bir_list:
        file_object.write(birlist+'\n')
    
