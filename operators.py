# -*- coding: utf-8 -*-
"""Operators.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bXt3dXua3Nwd2GHlYxzCsYMVml_DdAVo
"""

x = 10
y = 2
print(x/y)

x = 8
y = 3
print(x/y)

print(10/0)

x = 10
y = 2.5
print(x/y)

# exponential operators

10**2

print(10**-1)

10**0

10**2.5

# FLoor Divison operator

x = 10
y = 3
print(x//y)

print(x/y)

x = -10
y = 3
print(x//y)

# Modulus Opertaor

x = 10
y = 2.5
print (int(x/y))

print (10**-1)

15//2

-11%3

print(int(float("5.4")))

print(bool("True"))

int(True)

int(False)

bool(1)

bool(0)

bool(None)

bool('')

# Password Checker

pass1 = input('Enter the password')
pass2 = input('Re enter the password')
if pass1 == pass2:
  print('Password Match')
else:
  print('password mismatch')

print('cat'=='Cat')

# Assignment Operator
a = 100
print(a)

a = 200
print(a)

a = 100
print(id(a))

a = 100
b = 800
print(id(a)== id(b))

a = 10
a += 3
print(a)

a -= 3
print(a)

a *=3
print(a)

a = 2
a **=3
print(a)

a = 10
a %= 2
print(a)

print((2**2)==4)

print(25>50 or 1!= 2)

not False

# write a program for an ATM Machine that is running low on cash

amount = int(input('Enter the amount'))
print(amount == 500 or amount == 1000 or amount == 2000)

marks = int(input('Enter the Marks'))
print(marks >= 50 or marks <= 100)

from platform import python_version
print(python_version())

amount == 500 or 1000