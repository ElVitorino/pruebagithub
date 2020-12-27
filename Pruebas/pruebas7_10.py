# -*- coding: utf-8 -*- 
'''
Created on 7 oct. 2020

@author: V�ctor
'''

a = 2
b = 10
c = a | b
print (c)

d, e = 0, 1
while e < 10:
    print('e = ', e)
    print('d = ', d)
    a, b = a, a + b
