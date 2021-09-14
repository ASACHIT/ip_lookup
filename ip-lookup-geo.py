import json

import requests
from colorama import Fore

banner = """
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/ 
"""


class whois:
    def __init__(self):
        print(f"{Fore.LIGHTWHITE_EX}{banner}")
        print(f"{Fore.LIGHTGREEN_EX}Hit Enter Key':'Your ipadd' or input someone's ip")
        self.ipadd = (input(Fore.WHITE + "Input IP ~# ")).strip()

        if self.ipadd.startswith("127") or self.ipadd.startswith("192.168"):
            print(
                f"{Fore.RED} The Input Address is  local host"
                if self.ipadd.startswith("127")
                else "This Are Not Valid Ip Address :("
            )
            exit()

    def print_fetched(self):
        response = requests.get(f"http://ipwhois.app/json/{self.ipadd}")
        json_response = json.loads(response.text)
        for key, value in json_response.items():
            if value:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"{key.title()}: {Fore.WHITE} {str(value).strip()}"
                )


obj = whois()
obj.print_fetched()
