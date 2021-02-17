from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios
from global_var import *
from input import *


class ball_and_paddle:
    def chec(ball,x,pad):
        if ball._x >= pad._co and ball._x <= (pad._co + 7) :
            return True
        else :
            return False 
class ball_and_brick:
    def chec(ball,x):
        if x._grid[ball._y][ball._x] == Fore.RED + 'X' :
            x._grid[ball._y][ball._x] = Fore.YELLOW + '0'
            ball_and_brick.change_velo(ball)
            x._score +=1
            return True

        elif x._grid[ball._y][ball._x] == Fore.YELLOW + '0':
            x._grid[ball._y][ball._x] = Fore.GREEN + 'A'
            ball_and_brick.change_velo(ball)
            x._score +=1
            return True

        elif x._grid[ball._y][ball._x] == Fore.GREEN + 'A':
            x._grid[ball._y][ball._x] = Fore.BLACK + ' '
            ball_and_brick.change_velo(ball)
            x._score +=1
            return True

        elif x._grid[ball._y][ball._x] == Fore.LIGHTCYAN_EX + 'U':
            ball_and_brick.change_velo(ball)
            x._score +=1
            return True
            
    def change_velo(ball):
        if ball._velox > 0 and ball._veloy > 0:
            ball._velox = 0 - ball._velox
            ball._x = ball._x + ball._velox
        elif ball._velox < 0 and ball._veloy < 0:
            ball._velox = 0 - ball._velox
            ball._x = ball._x + ball._velox
        elif ball._velox > 0 and ball._veloy < 0:
            ball._veloy = 0 - ball._veloy
            ball._y = ball._y + ball._veloy
        elif ball._velox < 0 and ball._veloy > 0:
            ball._veloy = 0 - ball._veloy
            ball._y = ball._y + ball._veloy
        else :
            ball._veloy = 0 - ball._veloy
            ball._y = ball._y + ball._veloy

            
    
            

            
        



