from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios
from global_var import *


class static_bg:
    def __init__(self):
        self._lives = 2
        self._score = 0
        self._start = int(time.time())
        self._cn = 0
        self._grid = ([[Back.BLACK + Fore.BLACK + ' ' for col in range(cols)] for row in range(rows)])

        
        for val in range(cols):
            self._grid[0][val] = Fore.GREEN + '_'
            self._grid[2][val] = Fore.GREEN + '_'
            self._grid[rows - 1][val] = Fore.GREEN + '*'

        for val in range(1,rows-1):
            self._grid[val][0] = Fore.GREEN + '|'
            self._grid[val][cols-1] = Fore.GREEN + '|'
    
    def print_grid(x):
        info = "SCORE: " + str(x._score) + "|              Lives: " + str(x._lives) + "|            Time :" + str(int(time.time()) - x._start)
        for val in range(len(info)):
            x._grid[1][val+1] = Fore.GREEN + info[val]
        output_str = ""
        for row in range(rows):
            for col in range(cols):
                output_str += x._grid[row][col]
            
            output_str += "\n"
        print('\033[H' + output_str)
        print(Style.RESET_ALL)
