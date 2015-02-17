# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# 正则表达式基础

# <markdowncell>

# 在python中使用正则表达式的方法有两种，一种是直接使用re模块方法;另外一种是先将正则表达式编译成模式对象，然后使用模式对象方法。

# <headingcell level=2>

# 直接使用re模块方法

# <markdowncell>

# 在python中使用正则表达式时需要导入re模块

# <codecell>

import re

# <markdowncell>

# 定义需要匹配的文本串以及正则表达式

# <codecell>

text="220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
regex="220000|330000"

# <markdowncell>

# re模块的match方法从需要匹配的文本串开头以正则表达式规则开始匹配。

# <codecell>

re.match(regex,text).group()

# <markdowncell>

# re模块的search方法在整个需要匹配的文本串中以正则表达式规则进行匹配，匹配到一个字串即停止。

# <codecell>

re.search(regex,text).group()

# <markdowncell>

# re模块的findall方法在整个需要匹配的文本传中以正则表达式规则匹配出所有符合要求的字串。

# <codecell>

print re.findall(regex,text)

# <headingcell level=2>

# 使用正则表达式模式对象方法

# <markdowncell>

# 将正则表达式regex编译成模式对象，并将对象引用赋值给变量pattern。

# <codecell>

pattern = re.compile(regex)

# <markdowncell>

# 使用模式对象方法进行正则表达式匹配

# <codecell>

pattern.match(text).group()

# <codecell>

pattern.search(text).group()

# <codecell>

print pattern.findall(text)

# <headingcell level=2>

# 正则表达式中的特殊符号和字符

# <headingcell level=3>

# 1. ‘|’：或

# <markdowncell>

# ‘|’在正则表达式中用来将多种可能的匹配模式进行分隔，起到“或”的作用。

# <codecell>

regex='bat|bit|bet'
text='I bet it takes quite a bit of time to catch a bat.'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 2. ‘.’：用来替换任意一个字符，除了“\n”

# <codecell>

regex='b.t'
text='I bet it takes quite a bit of time to catch a bat.'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 3. '^' ：从需要匹配字符串开头进行匹配

# <markdowncell>

# textfile文件包含4行文本内容，下面将以textfile为基础进行正则表达式模式匹配

# <codecell>

!cat textfile

# <markdowncell>

# 匹配textfile文件内容中所有以‘d’开头的行

# <codecell>

regex="^d.*"
f = open("textfile",'r')
for eachLine in f:
    print re.compile(regex).findall(eachLine)

# <headingcell level=3>

# 4. '$' ： 从需要匹配的字符串的尾部进行匹配

# <markdowncell>

# 匹配textfile文件内容中所有以‘t’结尾的行

# <codecell>

regex=".*t$"
f = open("textfile",'r')
for eachLine in f:
    print re.compile(regex).findall(eachLine)

# <headingcell level=3>

# 5. 用来描述匹配模式重复次数的符号

# <headingcell level=4>

# ‘*’ ： 其前匹配模式重复0次或多次

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='go*gle'
print re.compile(regex).findall(text)

# <headingcell level=4>

# ‘+’ ： 其前匹配模式重复1次或多次

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='go+gle'
print re.compile(regex).findall(text)

# <headingcell level=4>

# ‘?’ ： 其前匹配模式重复1次或多次

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='go?gle'
print re.compile(regex).findall(text)

# <headingcell level=4>

# “{N}” ：其前匹配模式重复N次

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='go{4}gle'
print re.compile(regex).findall(text)

# <headingcell level=4>

# “{N,M}” ：其前匹配模式至少重复N次，最多重复M次

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='go{1,2}gle'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 6. [...] ：用来描述一个字符集合，匹配时只能匹配其中一个字符

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='b[ua][td]'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 7. [x-y] ： 以字符区间来描述一个字符集合，匹配时只能匹配其中一个字符

# <codecell>

text="The google is a good name,but the goooogle, gogle or ggle is a bad name."
regex='[a-zA-Z][a-z][a-z]'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 8. [^...] ： 在方括号中的'^'与在方括号外面的意义不同，这里表示‘反’的意思，即表示匹配除方括号内以外的字符

# <codecell>

text="I bet it takes quite a bit of time to catch a bat"
regex='b[^e]t'
print re.compile(regex).findall(text)

# <headingcell level=3>

# 9. (*|+|?|{})? ： 以非贪婪模式进行重复

# <codecell>

text="220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
regex='310000\|(.*?),'
results = re.compile(regex).findall(text)
for result in results:
    print result

# <markdowncell>

# 正则表达式“310000\|(.*?),”的匹配规则是在text中查找以“310000|”开头，以‘，’结尾之间的任意字符。"(.*?)"表示以非贪婪模式匹配到的任意字符。因此返回符合此模式最短的形式：“上海市”，如果以贪婪模式，则会获得以下结果，将返回符合次模式最长的形式：“上海市,320000|江苏省,330000|浙江省“

# <codecell>

text="220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
regex='310000\|(.*),'
results = re.compile(regex).findall(text)
for result in results:
    print result

# <headingcell level=3>

# 10. (...) ： 匹配结果将返回与圆括号中正则表达式匹配的字符串集。

# <codecell>

text = "220000|吉林省,310000|上海市,320000|江苏省,330000|浙江省,"
regex = "\|(.*?),"
results = re.compile(regex).findall(text)
for result in results:
    print result

# <headingcell level=3>

# 11. 正则表达式中的特殊字符

# <headingcell level=4>

# '\d'：等价于[0-9]; '\D'：等价于[^0-9]

# <codecell>

text = "file1.py,files.py"
regex = "file\d\.py"
print re.compile(regex).findall(text)

# <codecell>

text = "file1.py,files.py"
regex = "file\D\.py"
print re.compile(regex).findall(text)

# <headingcell level=4>

# '\w' ：等价于[a-zA-Z0-9\_]; '\W'：等价于[^a-zA-Z0-9\_]

# <codecell>

text = "file1.py,files.py,file_.py,file$.py"
regex = "file\w\.py"
print re.compile(regex).findall(text)

# <codecell>

text = "file1.py,files.py,file_.py,file$.py"
regex = "file\W\.py"
print re.compile(regex).findall(text)

# <headingcell level=4>

# '\s'：等价于[\n\t\r\v\f]; '\S'：等价于[^\n\t\r\v\f]

# <markdowncell>

# 执行who命令

# <codecell>

!who

# <markdowncell>

# 将who命令的输出重定向到”/home/whpuser/pythoncode/whooutput“中：

# <codecell>

!who > /home/whpuser/pythoncode/whooutput

# <markdowncell>

# 显示whooutput文件中的内容

# <codecell>

!cat whooutput

# <markdowncell>

# 将文件whooutput文件中的每一行以2个以上空白符进行分割：

# <codecell>

f = open('whooutput','r')
for eachLine in f:
    print re.split('\s\s+',eachLine)

# <codecell>


