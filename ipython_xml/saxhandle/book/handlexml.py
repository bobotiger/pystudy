#!/usr/bin/python
# coding=utf-8
import xml.sax
import bookhandler
#import studenthandler
import pprint

parser = xml.sax.make_parser()
handler = bookhandler.BookHandler()
#handler = studenthandler.StudentHandler()
parser.setContentHandler(handler)
parser.parse("books.xml")
#parser.parse("studentinfo.xml")
pprint.pprint(handler.mapping)
