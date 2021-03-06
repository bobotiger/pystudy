# --*-- coding=utf-8 --*--
from xml.sax import ContentHandler
class ArticleHandler(ContentHandler): #创建继承于ContentHandler类的子类
    """
    用于处理article.xml文档的内容事件处理器类
    """
    inArticle = 0	        #是否在webArticle元素中
    inBody = 0      	        #是否在body元素中
    isMatch = 0		        #是否找到所需元素
    title = ""			#类成员变量
    body = ""			#类成员变量
    
    def startElement(self,name,attrs):			#1.方法startElement重载
        if name == "webArticle":			#如果当前处理元素为webArticle
            subcat = attrs.get("subcategory","")        #获取该元素的属性subcategory的值
            if subcat.find("tech") > -1:		#如果属性值中包含"tech"
                self.inArticle = 1		
                self.isMatch = 1
        elif self.inArticle:				#如果在webArticle元素中
            if name == "header":			#如果当前处理元素为header
                self.title = attrs.get("title","")
            if name == "body":				#如果当前处理元素为body
                self.inBody = 1

    def characters(self,characters):		        #2.方法characters重载
        if self.inBody:					#如果在元素body中
            if len(self.body) < 80:
                self.body += characters
            if len(self.body) > 80:
                self.body = self.body[:78] + "..."
            self.inBody = 0				

    def endElement(self,name):				#3.方法endElement重载
        if name == "body":
            self.inBody = 0


