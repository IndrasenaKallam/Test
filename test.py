from colorama import Fore, init
# import getpass
import os


# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)


class config_gen:
    username = "indrasena"
    password = "kallam"
    name = {"servers": []}
    left1 = {"servers": []}
    right1 = {"servers": []}

    def __init__(self):
        print(Fore.BLUE + " please provide the credentials: ")
        # self.username = input("username is({}) : ".format(username)
        # self.password = getpass.getpass(prompt="enter the  password for %s: " % self.username)
        name = os.getenv("middle")
        print(type(name))
        left1 = self._physical_rack(name, -1)
        right1 = self._physical_rack(name, +1)
        print(left1)
        print(right1)
        print(name)

    @staticmethod
    def _physical_rack(name, incremental):
        return name[:-2] + "{0:0=2d}".format(int(name[-2:]) + incremental)

    def getting_arguments(self):
        print(self.username)
        print(self.password)


if __name__ == '__main__':
    generator = config_gen()
    generator.getting_arguments()
