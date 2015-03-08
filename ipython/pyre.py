#!/usr/bin/env python
# -*- coding=utf-8 -*-
import re
def printcomment(s):
    print "\033[1;32;40m",s,"\033[0m"

def printregex(regex,text):
    print "\033[1;31;40m",regex,"\033[0m",text

def regextest(regex,text):
    rem = re.match(regex,text)  #从text开头开始匹配regex，返回一个匹配的子串，没有匹配返回None
    res = re.search(regex,text) #在text中匹配regex，返回一个匹配的子串，没有匹配返回None
    if rem:
        print "re.match(regex,text) --> ",rem.group()
    if res:
        print "re.search(regex,text) --> ",res.group()
    pattern = re.compile(regex) #将正则表达式字符串编译成pattern对象
    print "re.compile(regex).findall(text) -->",pattern.findall(text)
#正则表达式中常用符号

#1. | : 或
printcomment("#1. | : 或")
regex='bat|bit|bet'
text='I bet it takes quite a bit of time to catch a bat.'
print(regex,text)
regextest(regex,text)

#2. . : 匹配任意字符，除了\\n
printcomment("#2. . : 匹配任意字符，除了\\n")
regex='b.t'
text='I bet it takes quite a bit of time to catch a bat.'
print(regex,text)
regextest(regex,text)

#3. ^ : 从字符串开头匹配
printcomment("#3. ^ : 从字符串开头匹配")
regex='^d.*'
f = open("textfile",'r')
i = 1
for eachLine in f:
    print "Line",i,":"
    print(regex,eachLine)
    print "re.compile(regex).findall(eachLine) -->",re.compile(regex).findall(eachLine)
    i += 1

#4. $ : 从字符串结尾匹配
printcomment("#4. $ : 从字符串结尾匹配")
regex='.*t$'
f = open("textfile",'r')
i = 1
for eachLine in f:
    print "Line",i,':'
    print(regex,eachLine)
    print "re.complie(regex).findall(eachLine) -->",re.compile(regex).findall(eachLine)
    i += 1
    
#5. * : 匹配0次或多次"*"之前的正则表达式
printcomment("#5. * : 匹配0次或多次'*'之前的正则表达式")
text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex=r'go*gle'
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#6. + : 匹配1次或多次"+"之前的正则表达式
printcomment("#6.+ : 匹配1次或多次'+'之前的正则表达式")
regex=r'go+gle'
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#7. ? : 匹配0次或1次"?"之前的正则表达式
printcomment("#7.? : 匹配0次或1次'?'之前的正则表达式")
regex=r'go?gle'
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#8. {N} : 匹配N次之前的正则表达式
printcomment("#8.{N} : 匹配N次之前的正则表达式")
regex=r'go{4}gle'
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#9. {M,N} : 匹配至少M次，最多N次之前的正则表达式
printcomment("#9.{M,N} : 匹配至少M次，最多N次之前的正则表达式")
regex=r'go{2,4}gle'
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#10. [...] : 匹配方括号中的任意一个字符
printcomment("#10. [...] : 匹配方括号中的任意一个字符")
regex='[ae]'
text="abcde"
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#11. [x-y] : 匹配从x开始到y之间的任意一个字符
printcomment("#11. [x-y] : 匹配从x开始到y之间的任意一个字符")
regex='[c-e]'
text="abcde"
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#12. [^...] : 不匹配方括号中的任意字符
printcomment("#12. [^...] : 不匹配方括号中的任意字符")
regex='[^c-e]'
text="abcde"
printregex(regex,text)
print "re.complie(regex).findall(text) -->",re.compile(regex).findall(text)

#13. (*|+|?|{})? : 以非贪婪模式匹配
printcomment("#13.(*|+|?|{})? : 以非贪婪模式匹配")
text="220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
greedy_regex='310000\|(.*),'
printregex(greedy_regex,text)
results = re.compile(greedy_regex).findall(text)
for result in results:
    print "结果:",result

non_greedy_regex = '310000\|(.*?),'
printregex(non_greedy_regex,text)
results = re.compile(non_greedy_regex).findall(text)
for result in results:
    print "结果:",result

#14. (...) : 匹配圆括号中封闭正则表达式，匹配的字符串作为结果，例如下面匹配出所有省名称
printcomment("#14. (...) : 匹配圆括号中封闭正则表达式，匹配的字符串作为结果，例如下面匹配出所有省名称")
text = "220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
regex = "\|(.*?),"
printregex(regex,text)
results = re.compile(regex).findall(text)
for result in results:
    print result
#正则表达式中的特殊字符
# \d : 匹配任意数字字符，等价于[0-9]。\D是\d的反
# \w : 匹配任意英文和数字字符，等价于[A-Za-z0-9_]。\W是\w的反
# \s : 匹配任意空白符，等价于[\n\t\r\v\f]。\S是\s的反
f = open('whooutput.txt','r')
for eachLine in f:
    print re.split(r'\s\s+',eachLine)
f.close()

