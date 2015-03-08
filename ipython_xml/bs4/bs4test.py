#!/usr/bin/env python

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
def printresult(s):
    print "\033[1;36;40m",s,"\033[0m","-->","\033[1;33;40m",eval(s),"\033[0m"

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

print "print a entire html file with a pretty format:"
print(soup.prettify())

print "print the components of html files:"
print soup.title
print soup.title.name
print soup.title.string
print soup.title.parent.name
print soup.p
print soup.p['class']
print soup.a
print soup.find_all('a')
print soup.find(id='link3')



