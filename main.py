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

con = Console()

def clscr():
    for i in range(200):
        print()

def mainMenu():
    clscr()
    banner = pyfiglet.figlet_format("    Cryptix",font="xtty")
    con.print(banner,style="bold green")



mainMenu()