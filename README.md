# Thunder_logagent
日志服务器的agent 

语言python2.7 支持centos系统(只在centos上测试过)

通过自动获取客户端的IP GET到服务器的API获取相应的配置文件，通过配置文件主动取日志，然后POST到服务器的API.

API 示例

urlpatterns = [

    url(r'^test/api',showlog_views.testapi),
    
    url(r'^test/setting',showlog_views.setting),
    
]

def setting(request):
    
    if request.GET['ip']:
    
        config={ "service": [{'zabbix':'/var/log/zabbix/zabbix_server.log'},{'httpd':'/var/log/httpd/access_log'}]}
        
        return HttpResponse(json.dumps(config))
        
    return HttpResponse()

def testapi(request):

    if 'table' in request.GET:
    
        return render(request,'api.html',{'hostip':request.GET['table']})
    
    return render(request,'api.html',{'hostip':"禁止"})
