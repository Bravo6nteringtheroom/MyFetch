import platform
import psutil
import os
import socket
from uptime import uptime

class OS:
    #OS info 
    OS_name = platform.platform()
    OS_version = platform.system()
    
    #Host name
    Hostname = socket.gethostname()
    
    #CPU info
    cpu_cores = os.process_cpu_count()
    cpu_type = platform.processor()
    cpu_usage = psutil.cpu_percent(interval=1)
    #RAM usage / total
    ram_used = round(psutil.virtual_memory().percent)
    ram_total = round(psutil.virtual_memory().total / (1024 ** 3))
    
    #IPAddr
    IP_Addr = socket.gethostbyname(Hostname)
    
    #Disk used / total
    storage_used = round((psutil.disk_usage('/').used / (1024 ** 3)))
    storage_total = round((psutil.disk_usage('/').total / (1024 ** 3)))
    #UpTime function
    uptime = round(uptime() / 3600)
