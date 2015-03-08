#!/usr/bin/env python
# -*- coding:utf-8 -*-

#内建iter函数
i = iter("abc")
print i.next(); #读取序列“abc”中的下一个数据
print i.next(); 
print i.next();
print i.__iter__(); #返回迭代器对象自身
print i.next(); #由于序列已经遍历完毕，此时再次调用next时会抛出StopIteration异常

