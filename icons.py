import types

from colorist import green, red, yellow
from Info import OS
import HexColors

#Hex HexColors
Hex = HexColors

Linux_icon = "\uf17c"
Mac_icon = "\ue711"
window_icon = "\uf17a"

cpu_icon = "\U000f0ee0"
IP_icon = "\U000f1982"
version_icon = "\ueb78"
Type_icon = "\uebba"
usage_icon = "\uedc8"
ram_icon = "\uF2DB"
Disk_icon = "\uf0c7"
clock_icon = "\U000f0954"
host_icon = "\ue0a2"
core_icon = "\uf305"

Info = OS()
def Check_version_for_icon():
    if(Info.Hostname == "Mac"):return  Mac_icon  
    elif(Info.Hostname == "Linux"):return Linux_icon
    else:return  window_icon


def Check_cpu_usage():
    if(Info.storage_used < Info.storage_total / 2):
        return f"{Hex.green}{Info.storage_used}{Hex.green.OFF}"
    elif(Info.storage_used == Info.storage_total / 2):
        return f"{Hex.yellow}{Info.storage_used}{Hex.yellow.OFF}"
    elif(Info.storage_used > Info.storage_total / 2):
        return f"{Hex.orange}{Info.storage_used}{Hex.orange.OFF}"
    else:
        return f"{Hex.red}{Info.storage_used}{Hex.red.OFF}"

def check_ram_usage():
    if(Info.ram_used < Info.ram_total / 2):
        return f"{Hex.green}{Info.ram_used}{Hex.green.OFF}"
    elif(Info.ram_used == Info.ram_total / 2):
        return f"{Hex.yellow}{Info.ram_used}{Hex.yellow.OFF}"
    elif(Info.ram_used > Info.ram_total/ 2 and Info.ram_used < Info.ram_total):
        return f"{Hex.orange}{Info.ram_used}{Hex.orange.OFF}"
    else:
        return f"{Hex.red}{Info.ram_used}{Hex.red.OFF}"

def check_Disk_usage():
    if(Info.storage_used < Info.storage_total / 2):
        return f"{Hex.green}{Info.storage_used}{Hex.green.OFF}"
    elif(Info.storage_used == Info.storage_total / 2):
        return f"{Hex.yellow}{Info.storage_used}{Hex.yellow.OFF}"
    else:
        return f"{Hex.red}{Info.storage_used}{Hex.red.OFF}"

#OS icon 
OS_icon =  Check_version_for_icon()

#Disk_icon_color 
Disk_icon = check_Disk_usage()

#Cpu_icon_color
Cpu_icon_color = Check_cpu_usage()

#Ram_icon_color
Ram_icon_color = check_ram_usage()
