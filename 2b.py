# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:36:53 2019

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
a1=a2=0

for i in range(inputs):
    p.append(int(lines[1+i*3]))
    #p.append(int(input()))
    gen.append(int(lines[2+i*3]))
    #gen.append(int(input()))
    y.append(int(lines[3+3*i]))
    #y.append(int(input()))
    
for i in range(inputs):
    if(pow(y[i],int((p[i]-1)/2),p[i]) == 1):
        a1 = 0
    else:
        a1=1
    z = (y[i] * pow(gen[i],p[i] - 1 - a1,p[i]))%p[i]
    if(pow(z,int((p[i]-1)/4),p[i]) == 1):
        a2 = 0
    else:
        a2=1
    ans.append(str(a2) + str(a1))
        
for a in ans:
    print(a)
