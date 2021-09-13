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
        print(Fore.LIGHTWHITE_EX + banner)
        print(Fore.LIGHTGREEN_EX + "'Hit Enter Key':'Your ipadd' or input someone's ip")
        self.ipadd = (input(Fore.WHITE + "Input ip ~# ")).strip()
        self.stripped_ip = str(self.ipadd)

        if not self.stripped_ip == "":
            if self.stripped_ip.startswith("127") or self.stripped_ip.startswith(
                "192.168"
            ):
                print(Fore.RED + "This Are Not Valid Ip Address :(")
                print(Fore.RED + "The Input Address is  local host")
                exit()
        else:
            self.stripped_ip = ""

    def fetchinfo(self):
        # response = requests.get(url=("http://ip-api.com/json/" + self.ipadd)).text
        response = requests.get(
            url=("http://ipwhois.app/json/" + self.stripped_ip)
        ).text  # for more info
        json_response = json.loads(response)
        return json_response

    def printdata(self):
        ip_details = self.fetchinfo()
        for key, value in ip_details.items():
            if value:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"{key.capitalize()}: {Fore.WHITE} {str(value).strip()}"
                )


obj = whois()
obj.fetchinfo()
obj.printdata()
