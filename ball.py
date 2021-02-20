from colorama import Fore, Back, Style
from global_var import *
from input import *
from collisons import *
from powerup import *
from paddle import paddle
from static_bg import static_bg
import random

class ball:
    def __init__(self,x):
        val = random.randint(0,6)
        self._thru = 0
        self._x = 40 + val
        self._val = val
        self._y = rows - 4
        self._velox = 0
        self._veloy = 0
        self._pow = 0
        self._power = []
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
                self._val = self._x - pad._co 
                if pad._stick == 1:
                    chec = True
                    while chec :
                        chec = paddle.imove(pad,x,self)
                        static_bg.print_grid(x)
                    
                    self._veloy = 0 - self._veloy
                    dist = pad._co + 3  - self._x
                    self._velox -= dist
                    return True
                self._veloy = 0 - self._veloy
                dist = pad._co + 3  - self._x
                self._velox -= dist
            else :
                return False
        else:
            chec = ball_and_brick.chec(self,x)
            if chec == True:
                val = random.randint(0,4)
                if val == 0 :
                    p = powerup(self._x,self._y)
                    self._power.append(p)
        x._grid[self._y][self._x] = Fore.WHITE + 'o'
        return True
        