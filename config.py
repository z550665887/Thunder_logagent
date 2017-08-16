configs ={
    #"Host":"10.90.10.104",
    "Server": "172.30.50.159",
    "ServerPort": 8000,
    "urls":{

        'get_configs' :'test/setting',  #acquire all the services will be monitored
        'service_report': 'test/api',

    },
    'RequestTimeout':30,
    'ConfigUpdateInterval': 10, #5 mins as default

}

