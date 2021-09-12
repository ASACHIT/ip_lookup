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
        self.strip = str(self.ipadd)

        if not self.strip == "":
            if self.strip.startswith("127") or self.strip.startswith("192.168"):
                print(Fore.RED + "This Are Not Valid Ip Address :(")
                print(Fore.RED + "The Input Address is  local host")
                exit()
        else:
            self.strip = ""

    def fetchinfo(self):
        self.r = requests.get(url=("http://ip-api.com/json/" + self.ipadd)).text
        self.r2 = requests.get(url=("http://ipwhois.app/json/" + self.ipadd)).text
        self.j_obj = json.loads(self.r)
        self.j_obj2 = json.loads(self.r2)

    def printdata(self):
        print(Fore.LIGHTWHITE_EX + "Status: ", Fore.WHITE + (self.j_obj["status"]))
        print(Fore.LIGHTWHITE_EX + "Country: ", Fore.WHITE + (self.j_obj["country"]))
        print(
            Fore.LIGHTWHITE_EX + "Country Code: ",
            Fore.WHITE + (self.j_obj["countryCode"]),
        )
        print(
            Fore.LIGHTWHITE_EX + "ProviceName: ",
            Fore.WHITE + (self.j_obj["regionName"]),
        )
        print(
            Fore.LIGHTWHITE_EX + "Provice: ",
            Fore.WHITE + (self.j_obj["region"]),
        )
        print(Fore.LIGHTWHITE_EX + "City: ", Fore.WHITE + (self.j_obj["city"]).strip())
        print(
            Fore.LIGHTWHITE_EX + "Latitude: ",
            Fore.WHITE + str((self.j_obj["lat"])).strip(),
        )
        print(
            Fore.LIGHTWHITE_EX + "Longitude: ",
            Fore.WHITE + str((self.j_obj["lon"])).strip(),
        )
        print(
            Fore.LIGHTWHITE_EX + "Timezone: ",
            Fore.WHITE + (self.j_obj["timezone"]).strip(),
        )
        print(Fore.LIGHTWHITE_EX + "ISP: ", Fore.WHITE + (self.j_obj["isp"]).strip())
        print(Fore.LIGHTWHITE_EX + "ORG: ", Fore.WHITE + (self.j_obj["org"]).strip())
        print(Fore.LIGHTWHITE_EX + "AS: ", Fore.WHITE + (self.j_obj["as"]).strip())
        print(Fore.LIGHTWHITE_EX + "Query: ", Fore.WHITE + (self.j_obj["query"]))
        print("")


obj = whois()
obj.fetchinfo()
obj.printdata()
