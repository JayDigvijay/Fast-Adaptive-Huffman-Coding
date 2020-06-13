# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 03:27:02 2020

@author: Prof. S.R.Singh
"""
import math
char = 'A';
d1 = {}
d2 = {}
d1['$'] = 0
for i in range(8):
    d1[char] = 0
    num = ord(char) + 1
    char = chr(num)


####################################################################################################

def Add_Front (ch, d1, d2):
    sym = []
    f = []
    F = []
    Dec_Code = []
    Code_Length = []
    total_count = 0
    d2.clear()
    d1[ch] += 1
    for x in d1:
        if(d1[x]):
            sym.append(x)
            total_count += d1[x]
    for i in range(0, len(sym)):
        x = sym[i]
        f.append(d1[x]/total_count)
        if i == 0:
            F.append(f[i])
            Dec_Code.append(f[i]/2)
        elif i > 0:
            F.append(F[i-1] + f[i])
            Dec_Code.append(F[i-1] + f[i]/2)
        Code_Length.append(math.ceil(math.log(1/f[i])/math.log(2)) + 1)
        code = ''
        for j in range (Code_Length[i]):
            Dec_Code[i] *= 2
            if Dec_Code[i] >= 1:
                code += '1'
                Dec_Code[i] -= 1
            elif Dec_Code[i] < 1:
                code += '0'
            
        d2[x] = code
        
        
####################################################################################################
        
        
def Remove_Front (ch, d1, d2):
    sym = []
    f = []
    F = []
    Dec_Code = []
    Code_Length = []
    total_count = 0
    d2.clear()
    d1[ch] -= 1
    for x in d1:
        if(d1[x]):
            sym.append(x)
            total_count += d1[x]
    for i in range(0, len(sym)):
        x = sym[i]
        f.append(d1[x]/total_count)
        if i == 0:
            F.append(f[i])
            Dec_Code.append(f[i]/2)
        elif i > 0:
            F.append(F[i-1] + f[i])
            Dec_Code.append(F[i-1] + f[i]/2)
        Code_Length.append(math.ceil(math.log(1/f[i])/math.log(2)) + 1)
        code = ''
        for j in range (Code_Length[i]):
            Dec_Code[i] *= 2
            if Dec_Code[i] >= 1:
                code += '1'
                Dec_Code[i] -= 1
            elif Dec_Code[i] < 1:
                code += '0'
            
        d2[x] = code       
        
        
