#encoding:utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getLink(html):
    reg = r'href="http://release\.(.+?)" '
    linkre = re.compile(reg)
    linklist = re.findall(linkre,html)
    return linklist


url = r'chrome-extension://bfbameneiokkgbdmiekhjnmfkcnldhhm/generated/view-link-information\.html'

html = getHtml(url)
linklist = getLink(html)

print linklist