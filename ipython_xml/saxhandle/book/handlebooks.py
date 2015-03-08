#!/usr/bin/env python
# --*-- coding=utf-8 --*--
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class BookHandler(ContentHandler):
    def __init__(self):
        self.inTitle = 0
        self.inAuthor = 0
        
    def startElement(self,name,attributes):
        if name == "book":
            self.isbn = attributes["isbn"]
            print "book:",self.isbn
        elif name == "title":
            self.inTitle = 1
        elif name == "author":
            self.inAuthor = 1

    def characters(self,data):
        if self.inTitle:
            print "\ttitle:",data
        elif self.inAuthor:
            print "\tauthor:",data

    def endElement(self,name):
        if name == "title":
            self.inTitle = 0
        elif name == "author":
            self.inAuthor = 0

bh = BookHandler()
parser = make_parser()
parser.setContentHandler(bh)
parser.parse("books.xml")


