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
from modules.read_readme import *
from modules.terminal_size import *
from modules.wifis import *


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
    print("\n"*200)

def mainMenu():
    clscr()
    banner = pyfiglet.figlet_format(" Cryptix ",font="banner3-D")
    con.print((":"*75 + "\n")*2 + banner + ":"*75,style="bold green")
    print()
    con.print("\n   1. Matrix\n   2. WIFI\n   3. full hacking screen")
    #menuAW = IntPrompt.ask("What do you pick? ",choices=['1','2','3',])
    #if menuAW == 1:
    #    matrix()
    #if menuAW == 2:
    #    wifihack()
    #if menuAW == 3:
    #    hackScreen()
    
def halfMatrix():
    terminal_size = getTermSize()

    symbols = ['1','0',' ',' ',' ',' ',' ']
    rd_line = []
    for i in range(1,(round(int(terminal_size[1])/2))):
        line = []
        pr_line = ""
        for i in range(1,(round(int(terminal_size[0])/2))):
            r_symbol = random.choice(symbols)
            line.append(r_symbol)
        for symb in line:
            pr_line = pr_line + symb
        rd_line.append(pr_line)

    return rd_line



if read_readmeMD:
    mainMenu()
    for line in halfMatrix():
        print(line)
else:
    print("\nPlease read README.md\n")
    exit()