# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:17:09 2020

@author: Prof. S.R.Singh
"""
import time
start_time = time.time()

from Front_TreeSFE import Add_Front as AF
from Front_TreeSFE import Remove_Front as RF
from Back_Tree import Code_Back as CB
from Back_Tree import Insert_Back as IB
from Back_Tree import Remove_Back as RB

Input = "ACECEF"

Special_Codeword = '$'
Time_Constant = 4

W = Special_Codeword
T = Time_Constant
Alphabet_Range = 8

FT = { }        ## Front Tree, d1
FTC = { }        ## Front Tree, d2
char = 'A'     
for i in range(Alphabet_Range):
    FT[char] = 0
    num = ord(char) + 1
    char = chr(num)
FT[W] = 0
AF(W, FT, FTC)
BT = []
char = 'A'
for i in range(Alphabet_Range):
    BT.append(char)
    num = ord(char) + 1
    char = chr(num)
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
CR2 = (bit_length)/len(Input)*100/8
print("Compression ratio is = ", CR2)
print("--- %s seconds ---" % (time.time() - start_time))