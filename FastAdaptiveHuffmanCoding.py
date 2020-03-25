# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:50:10 2020

@author: Digvijay Singh
"""
from Front_Tree import Add_Front as AF
from Front_Tree import Remove_Front as RF
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
    else:
        code = FTC[ch]
        OS.append(ch)
        OC.append(code)
        AF(ch, FT, FTC)
    print(OS)
    print(OC)
    if(count >= T):
        RF(Input[count-T], FT, FTC)
        IB(Input[count-T], BT)
        
    count = count + 1