from termcolor import colored
print(colored("*********************** Domain To IP Convertor *************************",'green'))

print(colored("*********************** Create By 0xSinper_IU  *************************",'red'))


import socket
import pyfiglet # banner package 
banner = colored(pyfiglet.figlet_format("IP Convertor "),'green') # use for banner

print(banner)

Domain_Name = input("Please , Enter Domain name : ")

ip = socket.gethostbyname(Domain_Name)

print("IP For {} : {}".format(Domain_Name,ip))