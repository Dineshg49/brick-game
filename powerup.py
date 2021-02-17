from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios
import random
from global_var import *
from input import *
from collisons import *


class powerup:
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._veloy = 1
        
    def move(self,x):
        
        if x._grid[self._y][self._x] == Fore.WHITE + 'M':
            x._grid[self._y][self._x] = Back.BLACK + ' '
        self._y += self._veloy

        if(self._y == rows-3):
            self._veloy = 0
        if x._grid[self._y][self._x] == Back.BLACK + Fore.BLACK + ' ':
            x._grid[self._y][self._x] = Fore.WHITE + 'M'