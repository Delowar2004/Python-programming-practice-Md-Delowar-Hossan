#!/usr/bin/env python3



#Get any website source code just one click


import turtle # import package
import urllib.request as u
import pyfiglet # Banner package

titel = pyfiglet.figlet_format("Programer Delowar.Designer ")
banner = pyfiglet.figlet_format("Source Code Downloader ") # use for banner
print(titel)
print(banner)

website_Domain = turtle.textinput("Domain Name ","Url Address") # animation input from user



source_code = u.urlopen(website_Domain)
source_code_read = source_code.read()
print(source_code_read) # print source code