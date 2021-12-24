# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:06:28 2019

@author: Mohammad_Younesi
"""

import sys

lines = sys.stdin.readlines()
inputs = int(lines[0])
#inputs = int(input())
p = []
gen = []
y = []  
ans = []

for i in range(inputs):
    p.append(int(lines[1+i*3]))
    #p.append(int(input()))
    gen.append(int(lines[2+i*3]))
    #gen.append(int(input()))
    y.append(int(lines[3+3*i]))
    #y.append(int(input()))
    
for i in range(inputs):
    if(pow(y[i],int((p[i]-1)/2),p[i]) == 1):
        ans.append(0)
    else:
        ans.append(1)
        
for a in ans:
    print(a)