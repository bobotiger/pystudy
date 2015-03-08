#!/usr/bin/env python
# -*- coding=utf-8 -*-
def printcomment(s):
    print "\033[1;32;40m",s,"\033[0m"

def printresult(s):
    print "\033[1;36;40m",s,"\033[0m","-->","\033[1;33;40m",eval(s),"\033[0m"

printcomment("1.数字常量")
print 1234,-24,0 #一般整数
print 99999999999999999L #长整型数(无限大小)
print 1.23,3.14e-10,4E210,4.0e+210 #浮点数
print 0177,0x9ff,0xFF #整数的八进制和十六进制数
print 3+4j,3.0+4.0j,3J #复数

printcomment("2.表达式操作符")
x,y,z=0,1,2
print 'x=',x,' y=',y,' z=',z

printcomment("\t三元选择表达式")
printresult("\tx if y else z")
printresult("\ty if x else z")

printcomment("\t逻辑操作符")
printresult('\tx or y')  #逻辑或
printresult('\tx and y') #逻辑与
printresult('\tnot x')   #逻辑非
printresult('\tnot y')

printcomment("\t比较操作符")
printresult('\tx<y,x<=y,x==y,x!=y,x>=y,x>y') #比较操作符

printcomment("\t对象身份测试操作符")
x1=x
print '\tx1=x'
printresult('\tx is y,x is not y,x1 is x')   #对象身份测试

printcomment("\t序列成员测试操作符")
s="str"
s1="string"
seq=[1,2,3,4]
print '\ts=',s,' s1=',s1,' seq=',seq
printresult('\ts in s1,x not in seq') #序列成员测试

printcomment("\t位操作符")
num1=0b10001000
num2=0b10101010
print '\tnum1=',bin(num1),' num2=',bin(num2)
printresult('\tbin(num1 | num2)') #按位或
printresult('\tbin(num1 ^ num2)') #按位异或
printresult('\tbin(num1 & num2)') #按位与
printresult('\tbin(num1 >> 2)')   #右移
printresult('\tbin(num2 << 2)')   #左移

printcomment("\t算术操作符")
x,y=4,3.0
printresult("\tx,y")
printresult("\t-x+y,x-y,x*y,x%y,x/y,x//y,-x,+x,~x,x**y")

printcomment("\t序列操作符")
seq=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'] #方括号用来创建列表对象
string="Hello Python!" #字符串也是一种序列
printresult("\tseq,string")
printresult("\tseq[0],string[3]")
printresult("\tseq[:3],string[3:]")
printresult("\tseq[3:5],string[6:12]")

