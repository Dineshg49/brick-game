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
from powerup import *


class ball:
    def __init__(self,x):
        val = random.randint(0,6)
        self._x = 40 + val
        self._val = val
        self._y = rows - 4
        self._velox = 0
        self._veloy = 0
        self._pow = 0
        if val == 0 :
            self._velox = -1
            self._veloy = -1
        if val == 1 :
            self._velox = -1
            self._veloy = -1
        if val == 2 :
            self._velox = -1
            self._veloy = -1
        if val == 3 :
            self._velox = 0
            self._veloy = -1
        if val == 4 :
            self._velox = 1
            self._veloy = -1
        if val == 5 :
            self._velox = 1
            self._veloy = -1
        if val == 6 :
            self._velox = 1
            self._veloy = -1
        
        x._grid[rows-4][self._x] = Fore.WHITE + 'o'


    def move(self,x,pad):
        x._grid[self._y][self._x] = Fore.BLACK + ' '
        self._x += self._velox
        self._y += self._veloy
       
        if self._x >= cols-1:
            self._velox = 0 - self._velox
            self._x = self._x + self._velox
        elif self._x <= 1 :
            self._velox = 0 - self._velox
        if self._y <= 3 :
            self._veloy = 0 - self._veloy
        elif self._y >= rows - 4:
            sim = ball_and_paddle.chec(self,x,pad)
            if sim == True:
                self._veloy = 0 - self._veloy
                dist = pad._co + 3  - self._x
                self._velox -= dist
            else :
                return False
        else:
            chec = ball_and_brick.chec(self,x)
            if chec == True:
                self._pow += 1
        x._grid[self._y][self._x] = Fore.WHITE + 'o'
        return True