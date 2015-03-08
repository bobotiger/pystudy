#!/usr/bin/env python
# -*- coding=utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import socket

baseurl = "http://dbmeizi.com/"
cg_num = '10'
#伪装浏览器，以免被封
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36'}
    req_timeout = 20
    try:
        req = urllib2.Request(url,None,req_header)
        page = urllib2.urlopen(req,None,req_timeout)
        html = page
    except urllib2.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return html

def page_loop(pageid):
    url = baseurl + 'category/' + '%s?p=%s' % (cg_num,pageid)
    print url
    page = user_agent(url)
    soup = BeautifulSoup(page)
    total_img = 0
    imgs = soup.find_all(['img'])
    for myimg in imgs:
        link = myimg.get('data-bigimg')
        total_img += 1
        print link
        content2 = user_agent(link).read()
        with open(u'../images'+'/'+link[-13:],'wb') as code:
            code.write(content2)
    print "from %s download %d pics" % (url,total_img)
    return total_img

page_start = 3
page_stop  = 4
total = 0
for i in range(page_start,page_stop):
    total += page_loop(i)

print "Total download %d picture" % total
