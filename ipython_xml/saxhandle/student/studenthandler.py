#  coding=utf-8
import xml.sax.handler
class StudentHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = 0
        self.mapping = {}
    
    def startElement(self, name, attributes):
        if name == "student":
            self.buffer = ""
            self.isbn = attributes["sid"]
        elif name == "name":
            self.inTitle = 1
    
    def characters(self, data):
        if self.inTitle:
            self.buffer += data
            print data
    
    def endElement(self, name):
        if name == "name":
            self.inTitle = 0
        self.mapping[self.isbn] = self.buffer
