import requests
from bs4 import BeautifulSoup
import re , time
from colorama import Back , Fore , Style

logo = '''
     ________ ____  ___  _______________ 
 __ / / __/ // / / / / |/ /_  __/ __/ _ \
/ // /\ \/ _  / /_/ /    / / / / _// , _/
\___/___/_//_/\____/_/|_/ /_/ /___/_/|_| 
                    Author:Vabro
                    Github: github.com/valaDevs
                                         
'''
print(Fore.LIGHTYELLOW_EX +logo)

target_url = input(Fore.GREEN +"[+] Enter Target URL: ")
try:
    get = requests.get(target_url)
    if get.status_code == 200:
        print(Fore.LIGHTRED_EX + f"[*] Finding js files in {target_url} !")
        soup = BeautifulSoup(get.text , 'html.parser')
        l = [i.get('src') for i in soup.find_all('script' , type('text/javascript')) if i.get('src')] 
        print(Fore.YELLOW+"[*] Found JS files , happy hacking :)")
        print("==============================================")
        for script in l:
            print(Fore.YELLOW+ script)
    else:
        print(Fore.RED + f"{target_url} is NOT ok")
except requests.exceptions.RequestException as e:
    raise SystemExit(f"{target_url}: is Not reachable , Check URL please ! \nErr: {e}")
