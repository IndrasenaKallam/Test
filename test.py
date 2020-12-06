import argparse
import getpass
from colorama import Fore, init
import getpass
import os



'''
parser = argparse.ArgumentParser(description='addition of two number')
parser.add_argument('-first', '--first_number', help='Enter the first number')
parser.add_argument('-second', '--second_number', help='Enter the first number')
opts = parser.parse_args()

print(opts)

'''

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)


class config_gen:
    username = os.getenv("username")
    password = os.getenv("password")
    
    def __init__(self):
        print(Fore.BLUE + " please provide the credentials: ")
        #self.username = input("username is({}) : ".format(username)
        #self.password = getpass.getpass(prompt="PDX-ENG password for %s: " % self.username)

    def getting_arguments(self):
        print(self.username)
        print(self.password)


if __name__ == '__main__':
    generator = config_gen()
    generator.getting_arguments()
