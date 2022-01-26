import time
import random
import os
import sys
import string
from rich.prompt import *
from rich.panel import *
from rich.progress import *
from rich.console import *
import pyfiglet
from read_readme import *

con = Console()

if read_readmeMD == False:
    readmd = Prompt.ask("\nDid you read README.md?",choices=['y','n'])
    if readmd == 'y':
        f = open("read_readme.py","w",encoding="UTF-8")
        f.write("read_readmeMD = True")
        f.close
        read_readmeMD = True
    if readmd == 'n':
        f = open("read_readme.py","w",encoding="UTF-8")
        f.write("read_readmeMD = False")
        f.close

def clscr():
    for i in range(200):
        print()

def mainMenu():
    clscr()
    banner = pyfiglet.figlet_format(" Cryptix ",font="banner3-D")
    con.print((":"*75 + "\n")*2 + banner + ":"*75,style="bold green")
    print()
    con.print("\n   1. Matrix")
    
    

if read_readmeMD:
    mainMenu()
else:
    print("\nPlease read README.md\n")
    exit()