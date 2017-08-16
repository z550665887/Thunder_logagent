# -*- coding: utf-8 -*-
import os
from collections import deque
import config
import base64

def service(name,pwd):											###主要逻辑 读取上次读取日志的行数并和日志现在的行数进行对比 
    numberlabel=int(getline(name,pwd))							###利用sed -n '1,2' /var/xx.log 命令读取中间的行数
    lines=[]													###更新config文件下的xx.txt里纪录的上次读取日志行数。
    numberline=int(os.popen('more {0}|wc -l'.format(pwd)).read())	
    try:
        if numberline > numberlabel:
            f=os.popen("sed -n '{0},{1}p' {2}".format(numberlabel+1,numberline,pwd))
            for line in f.readlines():
                lines.append(base64.b64encode(line))			###由于日志内容包含许多特殊字符，在json转换会报错 转化为base64
            changereadline(numberline,name)
        elif numberline < numberlabel:							###遇到日志文件进行切分时候，日志的行数比上次读取的日志行数小
            changereadline(0,name)								###重置上次读取的行数	
    except:
        return lines,0 
    return lines,numberline-numberlabel     
    
def changereadline(number,name):		###生成文件记录读取日志的行数
    #print "I have a change"+str(number)
    with open("configtxt/{0}.txt".format(name),'w') as f:
        f.write(str(number))

def getline(name,pwd):			###获取日志现在的行数
    try:
        open("configtxt/{0}.txt".format(name))
    except:
        changereadline(int(os.popen('more {0}|wc -l'.format(pwd)).read()),name)
    return int(open('configtxt/{0}.txt'.format(name)).read().replace('\n',''))

def getip():			###get IP 
    try:
        f=os.popen('ls /etc/sysconfig/network-scripts/|grep ifcfg-|grep -v lo').readlines()
        for line in f:
            m=os.popen('cat /etc/sysconfig/network-scripts/{0}|grep IPADDR'.format(line.replace('\n',''))).readlines()
            if m:
                break
        #print "get IP ADDR "+m[0].split('=')[1].replace('\n','')
        return m[0].split('=')[1].replace('\n','')
    except:
        pass
       
