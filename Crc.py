# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:28:05 2020

@author: Baraka
"""
from numpy.random import choice
def get(): 
    dividend=input('Enter data : ')
    divisor=input('Enter divisor : ')
    return dividend,divisor
def xor(a,b):
    result=[]
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
    return ''.join(result)
def all(dividend, divisor): 
    val=len(divisor)  
    crc=dividend[0 : val] 
    while val < len(dividend): 
        if crc[0] == '1': 
            crc = xor(divisor, crc) + dividend[val] 
        else:
            crc = xor('0'*val, crc) + dividend[val] 
        val += 1 
    if crc[0] == '1': 
        crc = xor(divisor, crc) 
    else: 
        crc= xor('0'*val, crc) 
    checkword = crc
    return checkword
def receiving_end():
    data,divisor=get()
    data=f"{data}{'0'*(len(divisor)-1)}"
    crc=all(data,divisor)
    data=f'{data[0:-(len(divisor)-1)]}{crc}'
    print(f"{'*'*20} SENDER's END {'*'*20}")
    print(f"Data sent : {data}")
    print(f"CRC       : {crc}")
    for d in range(len(data)):
        changebit=choice([True,False], p=[0.05,0.95])
        if changebit:
            data=data[:d]+str((int(data[d])+1)%2)+data[d+1:]
    crc=all(data,divisor)
    print()
    print(f"{'*'*20} RECEIVER's END {'*'*20}")
    print(f"Data Received : {data}")
    print(f"CRC           : {crc}")
    print()
    print(f"{'*'*20} CONCLUSION {'*'*20}")
    if int(crc,2)==0:
        print("Correct data received ")
    else:
        print("Incorrect data received ")
receiving_end()
