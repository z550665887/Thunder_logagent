# -*- coding: utf-8 -*-
#####Thunder logcenter agent	雷霆日志系统agent
####author zhangpc1
###V1.0.1
##
#

import service
import config
import time
import urllib
import urllib2
import threading
import json
import base64

class leitingagent(object):							###我是可爱的注释哈	

    def __init__(self):								###初始化
        self.services=self.getbackurl()
        self.timestart=time.time()
        self.printifeng()
        print self.services
    def foreverrun(self):							###foreverrun 就是一直跑的主程序
        while True:
            if time.time()-self.timestart>300:
                self.timestart=time.time()
                self.services=self.getbackurl()
            for keys in self.services['service'].keys():	
                print keys+self.services['service'][keys]
                t=threading.Thread(target=self.plugin,args=[keys,self.services['service'][keys]])
                t.start()
            time.sleep(config.configs['ConfigUpdateInterval'])     

    def plugin(self,name,pwd):		####多线程处理
        m,n=service.service(name,pwd)
        if n!=0:
            date={"table":{name:[IP,m,time.time()]}}	####聚合信息 做成一个大的JSON
            print name+IP
            self.url_request(date)
    
    def url_request(self,date):		####通过POST方法发送date到指定端口
        mainurl="http://{0}:{1}/{2}".format(config.configs['Server'],config.configs['ServerPort'],config.configs['urls']['service_report'])
        try:
            data_encode = urllib.urlencode(date)
           
            req = urllib2.Request(url=mainurl,data=data_encode)
            res_data = urllib2.urlopen(req,timeout=config.configs['RequestTimeout'])
            res = res_data.read()

        except:
            pass

    def getbackurl(self):	####通过GET方法向服务器取相关的配置文件 包括日志种类和日志的位置
        mainurl="http://{0}:{1}/{2}?ip={3}".format(config.configs['Server'],config.configs['ServerPort'],config.configs['urls']['get_configs'],IP)
       # try:
        print mainurl
        req=urllib2.Request(mainurl)
        req_data=urllib2.urlopen(req,timeout=config.configs['RequestTimeout'])
        print req_data
        return json.loads(req_data.read())
            
        #except:
        #    print "getconfigfaild"
        #    pass

    def printifeng(self):          ####通过base64方法 输出ifeng
        banner = 'IF8gIF9fCihfKS8gX3wgX19fIF8gX18gICBfXyBfCnwgfCB8XyAvIF8gXCAnXyBcIC8gX2AgfAp8IHwgIF98ICBfX' \
             'y8gfCB8IHwgKF98IHwKfF98X3wgIFxfX198X3wgfF98XF9fLCB8CiAgICAgICAgICAgICAgICAgIHxfX18vCg=='
		############################		
		# _  __					   #
		#(_)/ _| ___ _ __   __ _   #
		#| | |_ / _ \ '_ \ / _` |  #
		#| |  _|  __/ | | | (_| |  #
		#|_|_|  \___|_| |_|\__, |  #
		#		  		   |___/   #
		############################
        print  base64.b64decode(banner)
        
#if __name__=='main':
IP=service.getip()
f=leitingagent().foreverrun()
