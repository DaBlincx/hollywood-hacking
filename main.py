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
from fontlist import *

con = Console()

def clscr():
    for i in range(200):
        print()

def mainMenu():
    ##clscr()
    print("\n\n")
    print(f"{nr}/{len(fontlist)}\n{fontch}")
    banner = pyfiglet.figlet_format("Cryptix",font=fontch)
    f_banner = con.print(banner,style="bold green")
    time.sleep(0.01)
    f.write(f"\n\n{nr}/{len(fontlist)}\n{fontch}\n{f_banner}")

nr = 0
f = open("printfonts.txt","w",encoding="UTF-8")
for fontch in fontlist:
    nr += 1
    mainMenu()
f.close