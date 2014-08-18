#encoding:utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg|gif)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist


for a in range(999,1001):  
    url = r'http://jandan.net/ooxx/page-%d'% a
    print url

html = getHtml(url)
picturelist = getImg(html)

print picturelist
