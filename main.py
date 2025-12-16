import Logos
from uptime import uptime
from itertools import zip_longest
from Info import OS
import icons
import HexColors

p = OS()
Hex = HexColors

info_lines = [
    #Hostname:
    f"{Hex.brown}{icons.OS_icon} Host Name: {p.Hostname}{Hex.brown.OFF}",
    #IP Address:
    f"\033[1;33m{icons.IP_icon} IP Address: {p.IP_Addr}\033[0m",
    #OS_name:
    f"\033[1;34m{icons.window_icon} OS: {p.OS_name}\033[0m",
    #OS_version:
    f"\033[1;36m{icons.version_icon} Version: {p.OS_version}\033[0m",
    #cpu_type
    f"\033[1;35m{icons.cpu_icon} CPU Type: {p.cpu_type}\033[0m",
    #cpu_cores
    f"\033[1;32m{icons.core_icon} CPU Core: {p.cpu_cores}\033[0m",
    #cpu_usage
    f"\033[1;31m{icons.usage_icon} CPU Usage: {p.cpu_usage}%\033[0m",
    #ram_used / ram_total
    f"\033[1;33m{icons.ram_icon} RAM: {p.ram_used}%\033[0m",
    #sotrageused / storagetotal
    f"\033[1;36m{icons.usage_icon} DISK: {p.storage_used} / {p.storage_total} GB\033[0m",
    #Get the uptime
    f"\033[1;32m{icons.clock_icon} UpTime: {p.uptime}Hr\033[0m"
]

def Display(logo_icon , info_sys):
    print()
    for logo, info in zip_longest(logo_icon, info_sys, fillvalue=""):
        print(f"{logo}\t \t{info}")
        
Display(Logos.logo_lines2,info_lines)
