#!/usr/bin/env python
# -*- coding:utf-8 -*-
#1.循环处理列表的一般方法
numbers = range(10)
size = len(numbers)
evens_1 = []
i = 0
while i < size:
    if i % 2 == 0:
        evens_1.append(i)
    i += 1
print 'evens_1 = ',evens_1

#2.Python风格的列表推导方式:List comprehensions
evens_2 = [i for i in range(10) if i % 2 == 0]
print 'evens_2 = ',evens_2

#3.列表创建、循环处理列表、格式化输出
seq = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
i = 0
for element in seq:
    seq[i] = '%d: %s' % (i,seq[i])
    i += 1
print seq

#4.使用enumerate，枚举化列表
seq = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for i,element in enumerate(seq):
    seq[i] = "%d: %s" % (i,seq[i])
print seq

#5.结合自定义函数，使用列表推导完成
def _treatment(pos,element):
    return '%d: %s' % (pos,element)

seq = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
week = [_treatment(i,el) for i,el in enumerate(seq)]
print week

