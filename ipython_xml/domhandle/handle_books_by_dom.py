#!/usr/bin/env python
# --*-- coding=utf-8 --*--

from xml.dom import minidom

doc = minidom.parse("books.xml")

books = doc.getElementsByTagName("book");
for book in books:
    isbn = book.getAttribute("isbn")
    print "book:",isbn
    title = book.getElementsByTagName("title")[0].childNodes[0].nodeValue
    author = book.getElementsByTagName("author")[0].childNodes[0].nodeValue
    print "\ttitle:",title
    print "\tauthor:",author

