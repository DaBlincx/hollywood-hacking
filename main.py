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
from terminal_width import *

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
    con.print("\n   1. Matrix\n")
    matrix()
    
def matrix():
    terminal_width = getWidth()
    symbols = ['1','0',' ',' ',' ',' ',' ']
    for i in range(1,int(input("how many lines?: "))):
        line = []
        pr_line = ""
        for i in range(1,terminal_width):
            r_symbol = random.choice(symbols)
            line.append(r_symbol)
        for symb in line:
            pr_line = pr_line + symb
        con.print(pr_line,style="bold")
        time.sleep(0.01)


if read_readmeMD:
    mainMenu()
else:
    print("\nPlease read README.md\n")
    exit()