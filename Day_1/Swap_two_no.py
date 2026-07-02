# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 07:57:32 2026

@author: harpal
"""

#swap number without third variable 

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("Before Swapping \nNum1 :",num1," Num2 : ",num2)
# num1,num2=num2,num1
        #or
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After Swapping \nNum1 : ",num1," Num2 : ",num2)