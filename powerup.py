from colorama import Fore, Back, Style
from global_var import *
from input import *
from collisons import *
import time
import random

class powerup:
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._veloy = 1
        self._start = 0
        self._used = 0
        val = random.randint(0,4)
        self._type = val
        self._c = str(val)
        
    def move(self,x,pad,bal):
        if self._used == 1:
            return
        if x._grid[self._y][self._x] == Fore.MAGENTA + self._c:
            x._grid[self._y][self._x] = Back.BLACK + ' '
        self._y += self._veloy

        if(self._y == rows-3):
            if self._x >= pad._co and self._x <= pad._co + pad._size :
                self._start = int(time.time())
                if self._type == 0 :
                    expand_paddle.create(pad)
                elif self._type == 1:
                    shrink_paddle.create(pad)
                elif self._type == 2 :
                    speedball.create(bal)
                elif self._type == 3 :
                    thruball.create(bal)
                elif self._type == 4 :
                    stick.create(pad)
            
            self._used = 1
        if x._grid[self._y][self._x] == Back.BLACK + Fore.BLACK + ' ':
            x._grid[self._y][self._x] = Fore.MAGENTA + self._c
    
    def end(self,x,pad,bal):
        curr = int(time.time())

        if curr - self._start >= 10 and self._start != 0 :
            if self._type == 0 :
                expand_paddle.end(pad)
            elif self._type == 1:
                shrink_paddle.end(pad)
            elif self._type == 2 :
                speedball.end(bal)
            elif self._type == 3 :
                thruball.end(bal)
            elif self._type == 4 :
                stick.end(pad)
            self._start = 0


class expand_paddle(powerup):
    def create(pad):
        pad._size +=3
    def end(pad):
        pad._size -=3
    
class shrink_paddle(powerup):
    def create(pad):
        pad._size -=3
    def end(pad):
        pad._size +=3

class speedball(powerup):
    def create(ball):
        ball._velox +=1
    def end(ball):
        ball._velox -=1

class thruball(powerup):
    def create(ball):
        ball._thru = 1
    def end(ball):
        ball._thru = 0

class stick(powerup):
    def create(pad):
        pad._stick = 1
    def end(pad):
        pad._stick = 0
        