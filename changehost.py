#encoding:utf-8
import os

#prod
prodlist = ['10.10.99.108 tao.b5m.com',
        	'10.10.99.108 ucenter.b5m.com',
        	'10.10.99.108 pre.b5m.com',
        	'10.10.99.108 tao.b5mcdn.com',
        	'172.16.11.51 staticcdn.b5m.com',
        	'172.16.11.205 cdn.bang5mai.com',
        	'172.16.11.88 www.bugfree.com']

#release:80
releaselist = ['172.16.11.80  release.tao.b5m.com',
           	   '172.16.11.205 ucenter.b5m.com',
		   	   '172.16.11.205 pre.b5m.com',
               '172.16.11.51  tao.b5mcdn.com',    
               '172.16.11.51  staticcdn.b5m.com',
               '172.16.11.205 cdn.bang5mai.com',
               '172.16.11.88 www.bugfree.com']

#new release:205
newreleaselist = ['172.16.11.205  release.tao.b5m.com',#新增测试服务器
           	      '172.16.11.205 ucenter.b5m.com',
		   	      '172.16.11.205 pre.b5m.com',
                  '172.16.11.51  tao.b5mcdn.com',    
                  '172.16.11.51  staticcdn.b5m.com',
                  '172.16.11.205 cdn.bang5mai.com',
                  '172.16.11.88 www.bugfree.com']

#online
onlinelist = ['172.16.11.88 www.bugfree.com']

def release_test():
    output = open(r'e:\360Downloads\testhost.txt','w')
    for release in releaselist:
        print release
        output.write(release)
        output.write("\n")
    output.close()

def prod_test():
    output = open(r'e:\360Downloads\testhost.txt','w')
    for prod in prodlist:
        print prod
        output.write(prod)
        output.write("\n")
    output.close()

def newrelease_test():
    output = open(r'e:\360Downloads\testhost.txt','w')
    for newrelease in newreleaselist:
        print newrelease
        output.write(newrelease)
        output.write("\n")
    output.close()

def online_test():
	output = open(r'e:\360Downloads\testhost.txt','w')
	for online in onlinelist:
		print online 
		output.write(online)
		output.write("\n")
	output.close()

def change(environment):
    if environment == 'releasetest':
       release_test()
       environment = False
    elif environment == 'prodtest':
	     prod_test()

    elif environment == 'onlinetest':
	     online_test()

    elif environment == 'newreleasetest':
	     newrelease_test()

environment = raw_input('please input environmentname which you want to change to: ')
while environment :
	  change(environment)
	  if environment in ['Q','q','releasetest','prodtest','onlinetest','newreleasetest']:
	  	 environment = False
	  else:
	       environment = raw_input('please input environmentname which you want to change to: ')
	





'''备忘20140722
#buglist-禅道
172.16.11.88   www.bugfree.com


#prod上
#10.10.99.108 tao.b5m.com
#10.10.99.108 ucenter.b5m.com
#10.10.99.108 pre.b5m.com
#10.10.99.108 tao.b5mcdn.com 
#172.16.11.51 staticcdn.b5m.com
#172.16.11.205 cdn.bang5mai.com

#release上
172.16.11.80  release.tao.b5m.com
172.16.11.205 ucenter.b5m.com
172.16.11.205 pre.b5m.com
172.16.11.51  tao.b5mcdn.com    
172.16.11.51  staticcdn.b5m.com
172.16.11.205 cdn.bang5mai.com
#release新增测试服务器
#172.16.11.205 release.tao.b5m.com

#淘宝api测试
#172.16.11.80 tao.com'''