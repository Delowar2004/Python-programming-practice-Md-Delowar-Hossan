print("*********************** Domain To IP Convertor *************************")

print("*********************** Create By 0xSinper_IU  *************************")

import socket
import pyfiglet # banner package
banner = pyfiglet.figlet_format("IP Convertor ") # use for banner

print(banner)

Domain_Name = input("Please , Enter Domain name : ")

ip = socket.gethostbyname(Domain_Name)

print("IP For {} : {}".format(Domain_Name,ip))