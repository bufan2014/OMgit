#encoding:utf-8
import urllib
import re
import time
import random

#--------------子方法--------------
#煎蛋网抓取数据
def JiandanCatch(iStart=1,iEnd=694):	#（起始页码,终止页码）
	baseUrl=r'http://jandan.net/ooxx';	#主页，用来获取最大页数
	#网页格式,eg:http://jandan.net/ooxx/page-2#comments
	tempList=[];
	for i in range(iStart,iEnd+1):
		#拼接抓取页地址
		catchUrl="{0}/page-{1}#comments".format(baseUrl,i);
		html=urllib.request.urlopen(catchUrl).read().decode('utf-8');
		#洗数据
		html=re.sub("\\s",'',html);
		#抓取图片链接
		#print(html)
		html=re.findall(r'<ol.+</ol',html,re.MULTILINE|re.IGNORECASE);
		#print(html[0])
		if(len(html)!=1):
			continue
		tempImgList=re.findall(r'(?<=imgsrc=")http://.+?\.jpg',html[0],re.IGNORECASE|re.MULTILINE)
		#print(tempImgList)
		tempList+=tempImgList
	return tempList


#下载图片程序
def DownloadImgList(imgList):
	#图片保存目录
	OutPutDir=r'G:\Media\Images\MeiZi';
	for item in imgList:
		#新图片命名
		ltime=time.localtime()
		timeStr=time.strftime("%Y%m%d%H%M%S", ltime);
		picName="{0}_{1}.jpg".format(timeStr,str(random.randint(1,100)))
		#下载图片
		try:
			urllib.request.urlretrieve(item,"{0}\\{1}".format(OutPutDir,picName));
			print("抓得图片：{0}".format(item))
		except:
			print("抓取图片异常，图片名：{0}".format(item))
	return len(imgList);					   
#--------------主程序--------------
print("——————————————开始抓取——————————————")
ImgUrlList=[];		#图片链接地址
ImgUrlList=JiandanCatch(999,1001)	#获取链接
count=DownloadImgList(ImgUrlList)	#下载图片
print("——————————————抓取完成(抓得图片{0}张)——————————————".format(count))




	