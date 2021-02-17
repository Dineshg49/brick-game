import random
from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios
from global_var import *
from static_bg import static_bg
from input import *
from bricks import * 
from paddle import *
from ball import *
from powerup import powerup



class Initial:
    def run(self):
        x = static_bg()
        bricks(x)
        pad  = paddle(x)
        bal = ball(x)
        static_bg.print_grid(x)
        chec = True
        while x._lives > 0:
            while(chec):
              chec = pad.imove(x,bal)
              static_bg.print_grid(x)

            pad.move(x)
            over = ball.move(bal,x,pad)
            if bal._pow > 0 :
              bal._pow -=1
              p = powerup(bal._x,bal._y)
              x._cn +=1
            if x._cn > 0:
              powerup.move(p,x)
            static_bg.print_grid(x)
            pad.move(x)
            if over == False:
              x._lives -= 1
              over = True
              pad = paddle(x)
              bal = ball(x)
              chec = True
            time.sleep(0.1)


