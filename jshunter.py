import requests
from bs4 import BeautifulSoup
import re , time
from colorama import Back , Fore , Style

logo = '''
   d88b .d8888. db   db db    db d8b   db d888888b d88888b d8888b. 
   `8P' 88'  YP 88   88 88    88 888o  88 `~~88~~' 88'     88  `8D 
    88  `8bo.   88ooo88 88    88 88V8o 88    88    88ooooo 88oobY' 
    88    `Y8b. 88~~~88 88    88 88 V8o88    88    88~~~~~ 88`8b   
db. 88  db   8D 88   88 88b  d88 88  V888    88    88.     88 `88. 
Y8888P  `8888Y' YP   YP ~Y8888P' VP   V8P    YP    Y88888P 88   YD 
                                                                             
                    Author:Vabro
                    Github: github.com/valaDevs
                                         
'''
print(Fore.LIGHTYELLOW_EX +logo)

target_url = input(Fore.GREEN +"[+] Enter Target URL (with https:// ): ")
try:
    get = requests.get(target_url)
    if get.status_code == 200:
        print(Fore.MAGENTA + f"[*] Finding js files in {target_url} !")
        soup = BeautifulSoup(get.text , 'html.parser')
        l = [i.get('src') for i in soup.find_all('script' , type('text/javascript')) if i.get('src')] 
        print(Fore.YELLOW+"[*] Found JS files , happy hacking :)")
        print("==============================================")
        for script in l:
            print(Fore.YELLOW+ script)
    else:
        print(Fore.RED + f"{target_url} is NOT ok")
except requests.exceptions.RequestException as e:
    raise SystemExit(Fore.RED + f"{target_url}: is Not reachable , Check URL please ! \nErr: {e}")
