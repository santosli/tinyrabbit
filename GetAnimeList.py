#!/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
from lxml import etree
import datetime
import sys


def GetListFromURL():	
	response = urllib2.urlopen("http://bt.ktxp.com/playbill.php")
	html = response.read().decode('utf-8')

	#print html

	tree = etree.HTML(html)

	f = open('AnimeList.txt','w')

	for i in range(1,8):
		path = u"//dl[%s]/dd/a" % (i)
		print >> f, i
		hrefs = tree.xpath(path)
		for href in hrefs:
			print >> f, href.text.encode("utf-8")

	f.close()

def GetListFromHTML():
	f = open('AnimeList.html')
	html = f.read().decode("utf-8")
	#print html

	tree = etree.HTML(html)

	date = datetime.datetime.now()
	week = date.weekday()

	if week == 0:
		week = 7

	#print week
	weekCh = [u'神',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日']

	anime = tree.xpath(u"//div")

	print u"今日是" + weekCh[week] + ":" + anime[week].text



if __name__ == "__main__":
	GetListFromHTML()