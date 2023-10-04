# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Exercise 2: 99乘法表
for i in range (1, 10):
    for j in range (1,10):
        product = i * j
        print("%d * %d = %2d " % (i,j,product), end = "")
    print()
