#encoding:utf-8
import re
import urllib

#定义函数获取html
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#定义函数获取imglist
def getImg(html):
    reg = r'src="(.+?\.jpg|gif)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

#定义函数获取最新页
def getnewest(html):
    reg = r'<span class="current-comment-page">.\d+.</span> '
    zhu = re.compile(reg) 
    zhulian = re.findall(zhu,html)
    newest = re.findall(r'\d+',zhulian[0])
    return int(newest[0])
   
#获取最新页
Url = r'http://jandan.net/ooxx'    
Html = getHtml(Url)
newest = getnewest(Html)   

#获取每页的url
for a in range(1160,newest+1):
    url = r'http://jandan.net/ooxx/page-%d'% a
    print url  

#获取图片链接
html = getHtml(url)
picturelist = getImg(html)
print picturelist

#图片链接list形式转成需要的字符串形式
picturestr1 = str(picturelist) #picturelist转换为字符格式
picturestr2 = picturestr1.replace('[',' ')
picturestr3 = picturestr2.replace(']','')
picturestr4 = picturestr3.replace(",",'\n')
picturestr5 = picturestr4.replace('\'','')

#保存图片链接
new_path_filename = 'e:\\360Downloads\\zhuatu.txt' #可以自定义path
f = open(new_path_filename,'w')
f.write(picturestr5)
f.close()