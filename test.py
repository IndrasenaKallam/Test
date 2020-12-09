import argparse
import getpass
from colorama import Fore, init
import getpass
import os


# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)


class config_gen:
    username = os.getenv("username")
    password = os.getenv("password")
    name = {"servers":[]}
    name1 = {"servers":[]}

    def __init__(self):
        print(Fore.BLUE + " please provide the credentials: ")
        # self.username = input("username is({}) : ".format(username)
        # self.password = getpass.getpass(prompt="enter the  password for %s: " % self.username)
        name = os.getenv(name)

    def getting_arguments(self):
        print(self.username)
        print(self.password)


if __name__ == '__main__':
    generator = config_gen()
    generator.getting_arguments()
