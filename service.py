import os
from collections import deque




def service(lastline):
    list=deque()
    key = 0
    with os.popen("tail -10 /var/log/zabbix/zabbix.log") as f:
        for line in f.readline():
            list.append(line) if key==1 else ""
            key = 1 if line == lastline and key == 0 else 0
    return 0 if list else return list

