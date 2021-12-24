# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:15:55 2019

@author: Mohammad_Younesi
"""


import sys
import math

#lines = sys.stdin.readlines()
#inputs = int(lines[0])
inputs = int(input())
p = []
gen = []
y = []  
ans = []
a1=a2=0

for i in range(inputs):
    #p.append(int(lines[1+i*3]))
    p.append(int(input()))
    #gen.append(int(lines[2+i*3]))
    gen.append(int(input()))
    #y.append(int(lines[3+3*i]))
    y.append(int(input()))
    
ans=[]
for i in range(int(inputs)):
    ans1 = []
    if(pow(y[i],int((p[i]-1)/2),p[i]) == 1):
        a1 = 0
    else:
        a1=1
    ans1.append(a1)
    myPow = p[i] - 1
    for j in range(int(math.log2(p[i]))-1):
        z = (y[i] * pow(gen[i],myPow - pow(2,j)*a1,p[i]))%p[i]
        myPow -= pow(2,j)*a1
        if(pow(z,int((p[i]-1)/(2**(j+2))),p[i]) == 1):
            a1 = 0
        else:
            a1=1
        ans1.append(a1)
        
        
    number=0
    for k in range(len(ans1)):
        number += ans1[k] * pow(2,k)
    if(number==0):
        number = p[i] - 1
    ans.append(number)    
for a in ans:
    print(a)
