#!/usr/bin/env python
# -*- coding=utf-8 -*-
X=99 #全局变量，在本文件中有效

def myfunc1():
    X=88 #局部变量，在函数中有效
    print 'myfunc1:',X

myfunc1()
print X

def myfunc2(Y):
    Z = X + Y
    print 'myfunc2:',Z

myfunc2(1)

def myfunc3():
    global X
    X = 66

myfunc3() #对全局变量X赋值
print X


