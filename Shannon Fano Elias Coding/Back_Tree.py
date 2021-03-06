# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:57:00 2020

@author: Digvijay Singh
"""


########DEFINING THE BACK TREE WITH 26 LETTERS###########


########################################################
def Code_Back(l):
    if(l == 1):
        return ['0']
    elif(l == 2):
        return ['0', '1']
    elif(l == 3):
        return ['00', '01', '1']
    elif(l == 4):
        return ['00', '01', '10', '11']
    elif(l == 5):
        return ['000', '001', '01', '10', '11']
    elif(l == 6):
        return ['000', '001', '01', '100', '101', '11']
    elif(l == 7):
        return ['000', '001', '010', '011', '100', '101', '11']
    elif(l == 8):
        return ['000', '001', '010', '011', '100', '101', '110', '111']
    elif(l == 9):
        return ['0000', '0001', '001', '010', '011', '100', '101', '110', '111']
    elif(l == 10):
        return ['0000', '0001', '001', '010', '011', '1000', '1001', '101', '110', '111']
    elif(l == 11):
        return ['0000', '0001', '001', '0100', '0101', '011', '1000', '1001', '101', '110', '111']
    elif(l == 12):
        return ['0000', '0001', '001', '0100', '0101', '011', '1000', '1001', '101', '1100', '1101', '111']
    elif(l == 13):
        return ['0000', '0001', '0010', '0011', '0100', '0101', '011', '1000', '1001', '101', '1100', '1101', '111']
    elif(l == 14):
        return ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '101', '1100', '1101', '111']
    elif(l == 15):
        return ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '111']
    elif(l == 16):
        return ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    elif(l == 17):
        return ['00000', '00001', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    elif(l == 18):
        return ['00000', '00001', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '10000', '10001', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    elif(l == 19):
        return ['00000', '00001', '0001', '0010', '0011', '01000', '01001', '0101', '0110', '0111', '10000', '10001', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    elif(l == 20):
        return ['00000', '00001', '0001', '0010', '0011', '01000', '01001', '0101', '0110', '0111', '10000', '10001', '1001', '1010', '1011', '11000', '11001', '1101', '1110', '1111']
    elif(l == 21):
        return ['00000', '00001', '0001', '00100', '00101', '0011', '01000', '01001', '0101', '0110', '0111', '10000', '10001', '1001', '1010', '1011', '11000', '11001', '1101', '1110', '1111']
    elif(l == 22):
        return ['00000', '00001', '0001', '00100', '00101', '0011', '01000', '01001', '0101', '01100', '01101', '0111', '10000', '10001', '1001', '1010', '1011', '11000', '11001', '1101', '1110', '1111']
    elif(l == 23):
        return ['00000', '00001', '0001', '00100', '00101', '0011', '01000', '01001', '0101', '01100', '01101', '0111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '1110', '1111']
    elif(l == 24):
        return ['00000', '00001', '0001', '00100', '00101', '0011', '01000', '01001', '0101', '01100', '01101', '0111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 25):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '0011', '01000', '01001', '0101', '01100', '01101', '0111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 26):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '0101', '01100', '01101', '0111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 27):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '0111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 28):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '1001', '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 29):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011',  '10100', '10101', '1011', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 30):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011',  '10100', '10101', '10110', '10111', '11000', '11001', '1101', '11100', '11101', '1111']
    elif(l == 31):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011',  '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '1111']
    elif(l == 32):
        return ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011',  '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']

def Insert_Back(c, letters):
    if c in letters:
        return
    letters.append(c)
    letters.sort()

def Remove_Back(c, letters):
    for x in letters:
        if(x == c):
            letters.remove(x)
            break
   
    
#Code = Code_Back(1)
#print(Code)   