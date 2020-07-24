# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:54:20 2020

@author: rohan.john
"""

list1=["Mr Issac Newton", "Mr Nicola Tesla"]
list2=[]
empty=[" "]

for i in range (0,len(list1)):
    a=list1[i].split()
    k=a[0]+ empty[0] + a[-1]
    list2.append(k)
    
print(list2)    
print(list1)
