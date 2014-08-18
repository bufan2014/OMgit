#encoding:utf-8
import os,glob
import re,pymongo
#-----连接MongoDB-----
conn = pymongo.Connection("localhost",27017)
db = conn.bufan_database
lianjie = db.bufan_collection

#要存储的文本
file = open("zhuatu.txt","r")

#用于存储每一条记录的swiftnum值，以防止重复插入
links = open("links.txt","r+")

#每条记录转成BSON文档时，每个域对应的key
keyarray = ["link"]
#分解文本记录用到的正则
pattern = r' \n*'
#包含数据库中已有的记录的swiftnum的list
link_list = links.read().split(",")
for line in file.readlines()[1:]: 
     i = 0
     data = {}
     li_list = re.split(pattern,line) #分解记录为list
for field in li_list:
     data[keyarray[i]]=field #将记录转为BSON文档
     i +=1
if data['link'] not in link_list: #判断是否重复
lianjie.insert(data)
links.write(data['link']+",") #记录已有记录
links.close()