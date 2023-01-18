import os
import random
import requests
import threading
from numerize import numerize
from colorama import Fore, Back, Style
os.system(f'title Shuttle Network Click Bot')
class a():
    s = 0
    f = 0


os.system("cls")
print(Fore.WHITE + '''
                           
     _       _   _   _     
 ___| |_ _ _| |_| |_| |___ 
|_ -|   | | |  _|  _| | -_|
|___|_|_|___|_| |_| |_|___|
                           
                                  \n\n\n''' + Style.RESET_ALL)
welcome = input(Fore.GREEN + "Welcome to Shuttle click Bot! Press Enter to continue" + Style.RESET_ALL)
threads = int(input(Fore.RED + "\n" * 5 + "Threads --> " + Fore.GREEN))
code = input(Fore.RED + "Link --> " + Fore.GREEN)


def click():
    try:
        os.system(f"title discord.gg/twitchtv ^| Success: {numerize.numerize(a.s)} ^| Failed {numerize.numerize(a.f)}")

        proxys = open('proxies.txt', 'r').read().splitlines()
        proxy = random.choice(proxys)
        proxies = {'http': f'http://{proxy}', 'https':f'http://{proxy}'}

        headers = {
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        r = requests.get(f"{code}", headers=headers, proxies=proxies)
        a.s += 1
    except:
        a.f += 1

while True:
    if threading.active_count() < threads:
        for x in range(threads):
            threading.Thread(target=click).start()
