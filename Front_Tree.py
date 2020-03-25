# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:53:19 2020

@author: Digvijay Singh
"""
import operator
char = 'A';
d1 = {}
d2 = {}
for i in range(8):
    d1[char] = 0
    num = ord(char) + 1
    char = chr(num)
d1['$'] = 0
###########################################################################
    
    
def Add_Front(ch, d1, d2):
    count = 0
    d2.clear()
    d1[ch] += 1
    l = [x for (x,y) in sorted(d1.items(), key=operator.itemgetter(1), reverse = True)]
    
    d2['$'] = ''
    for x in l:
        if(d1[x]):
            count += d1[x]
            d2[x] = ''
    for x in d2:
        flag = 0
        if(x == '$'):
            if(d1[x] >= 0.5 * count):
                d2[x] += '0'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '1'
                    if(y == x):
                        flag = 1
            elif(d1[x] < 0.5 * count):
                d2[x] += '1'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '0'
                    if(y == x):
                        flag = 1
        else:
            if(d1[x] < count):
                d2[x] += '0'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '1'
                    if(y == x):
                        flag = 1
                
        count -= d1[x]
    
###############################################################################
        
def Remove_Front(ch, d1, d2):
    count = 0
    d2.clear()
    d1[ch] -= 1
    l = [x for (x,y) in sorted(d1.items(), key=operator.itemgetter(1), reverse = True)]
    
    d2['$'] = ''
    for x in l:
        if(d1[x]):
            count += d1[x]
            d2[x] = ''
    for x in d2:
        flag = 0
        if(x == '$'):
            if(d1[x] >= 0.5 * count):
                d2[x] += '0'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '1'
                    if(y == x):
                        flag = 1
            elif(d1[x] < 0.5 * count):
                d2[x] += '1'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '0'
                    if(y == x):
                        flag = 1
        else:
            if(d1[x] < count):
                d2[x] += '0'
                for y in d2:
                    if(flag == 1):
                        d2[y] += '1'
                    if(y == x):
                        flag = 1
                
        count -= d1[x]    
        
#Add_Front('$', d1, d2)
#Add_Front('A', d1, d2)
#print(d2)