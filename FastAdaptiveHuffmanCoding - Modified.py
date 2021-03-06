# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:50:10 2020

@author: Digvijay Singh
"""
import time
start_time = time.time()

from Front_Tree import Add_Front as AF
from Front_Tree import Remove_Front as RF
from Back_Tree import Code_Back as CB
from Back_Tree import Insert_Back as IB
from Back_Tree import Remove_Back as RB

Input = "ACECEF"

for s in Input:
    if(ord(s) >= 97):
        s_new = chr(ord(s) - 32)
        Input = Input.replace(s, s_new)

Special_Codeword = '$'
Time_Constant = 4

W = Special_Codeword
T = Time_Constant
Alphabet_Range = 26

FT = { }        ## Front Tree, d1
FTC = { }        ## Front Tree, d2
char = 'A'     
for i in range(Alphabet_Range):
    FT[char] = 0
    num = ord(char) + 1
    char = chr(num)
FT[W] = 0
FT['.'] = 0
FT[','] = 0
FT['('] = 0
FT[')'] = 0
FT['-'] = 0
FT[' '] = 0
AF(W, FT, FTC)


BT = []
BTC = []
char = 'A'
for i in range(Alphabet_Range):
    BT.append(char)
    num = ord(char) + 1
    char = chr(num)
BT.append('.')
BT.append(',')
BT.append('(')
BT.append(')')
BT.append('-')
BT.append(' ')
OS = []         ## Output Symbols
OC = []         ## Output Code
Newly_Added = []
count = 0
for ch in Input:
    if (ch in BT):
        BTC = CB(len(BT))
        code = BTC[BT.index(ch)]
        RB(ch, BT)
        if (count > 0):
            OC.append(FTC[W])
            OS.append(W)
            AF(W, FT, FTC)
        AF(ch, FT, FTC)
        OC.append(code)
        OS.append(ch)
        Newly_Added.append(1)
    else:
        code = FTC[ch]
        OS.append(ch)
        OC.append(code)
        AF(ch, FT, FTC)
        Newly_Added.append(0)
   
    if(count >= T):
        if Newly_Added[count-T] == 1:
            RF(W, FT, FTC)
        RF(Input[count-T], FT, FTC)
        IB(Input[count-T], BT)
        
    count = count + 1


print(OS)
print(OC)
bit_length = 0
for code in OC:
    bit_length += len(code)
CR1 = (bit_length)/len(Input)*100/8
print("Compression ratio is = ", CR1)    
print("--- %s seconds ---" % (time.time() - start_time))