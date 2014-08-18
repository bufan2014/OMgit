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

def getnewest(html):
    reg = r'<span class="current-comment-page">.\d+.</span> '
    zhu = re.compile(reg) 
    zhulian = re.findall(zhu,html)
    newest = re.findall(r'\d+',zhulian[0])
    return int(newest[0])
   

Url = r'http://jandan.net/ooxx'    
Html = getHtml(Url)
newest = getnewest(Html)   

for a in range(1160,newest+1):
    url = r'http://jandan.net/ooxx/page-%d'% a
    print url  

html = getHtml(url)
picturelist = getImg(html)

print picturelist
