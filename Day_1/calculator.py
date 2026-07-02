# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 07:56:17 2026

@author: harpal
"""

# print(eval(input("perform operation : "))) #calculate directly

# Menu Driven Calculator
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("\n" + "*" * 10 + " MENU " + "*" * 10)
print("+  : Addition")
print("-  : Subtraction")
print("*  : Multiplication")
print("/  : Division")
print("%  : Modulus")
print("** : Power")
print("*" * 26)

choice = input("Enter your choice (+, -, *, /, %, **) : ")

if choice == "+":
    print("Addition =", num1 + num2)

elif choice == "-":
    print("Subtraction =", num1 - num2)

elif choice == "*":
    print("Multiplication =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

elif choice == "%":
    if num2 != 0:
        print("Modulus =", num1 % num2)
    else:
        print("Error: Modulus by zero is not allowed.")

elif choice == "**":
    print("Power =", num1 ** num2)

else:
    print("Invalid Choice! Please select a valid operator.")