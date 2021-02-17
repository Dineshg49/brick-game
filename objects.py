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


class bricks:
    def __init__(self,x):
        with open('bricks.txt' , 'rb') as f:
           arr = []
           for line in f:
               arr.append(line)
               l = len(line)
        f.close()
        curr_row = 4
        
        for row in range(len(arr)):
            curr_col = 4
            for col in range(len(arr[row])-1):
                ch = chr(arr[row][col])
                if ch == 'X':
                    x._grid[curr_row][curr_col] =  Fore.RED + chr(arr[row][col])
                elif ch == '0':
                    x._grid[curr_row][curr_col] =  Fore.YELLOW + chr(arr[row][col])
                elif ch == 'A':
                    x._grid[curr_row][curr_col] =  Fore.GREEN + chr(arr[row][col])
                elif ch == 'U':
                    x._grid[curr_row][curr_col] =  Fore.LIGHTCYAN_EX + chr(arr[row][col])
                curr_col +=1
            curr_row +=1

class paddle:
    def __init__(self,x):
        with open('paddle.txt' , 'rb') as f:
           arr = []
           for line in f:
               arr.append(line)
               l = len(line)
        f.close()
        curr_row = rows-3
        self._co = 40        

        for row in range(len(arr)):
            curr_col = self._co
            for col in range(1,cols-1):
                 x._grid[curr_row][col] =  Fore.BLACK + ' '
            for col in range(len(arr[row])-1):
                x._grid[curr_row][curr_col] =  Fore.YELLOW + chr(arr[row][col])
                curr_col +=1
            curr_row +=1
    
    def imove(self,x,bal):
        with open('paddle.txt' , 'rb') as f:
           arr = []
           for line in f:
               arr.append(line)
               l = len(line)
        f.close()
        curr_row = rows - 3
        val = input_to(Get()) 
        if val == 'a' :
            if self._co != 1 :
                self._co -=1
        elif val == 'd':
            if self._co != cols-8 :
                self._co +=1
        elif val == 's' :
            return False

        x._grid[bal._y][bal._x] = Fore.BLACK + ' '
        bal._x = bal._val + self._co
        x._grid[bal._y][bal._x] = Fore.WHITE + 'o'
        for row in range(len(arr)):
            curr_col = self._co
            for col in range(1,cols-1):
                 x._grid[curr_row][col] =  Fore.BLACK + ' '
            for col in range(len(arr[row])-1):
                x._grid[curr_row][curr_col] =  Fore.YELLOW + chr(arr[row][col])
                curr_col +=1
            curr_row +=1
        
        return True
    
    def move(self,x):
        with open('paddle.txt' , 'rb') as f:
           arr = []
           for line in f:
               arr.append(line)
               l = len(line)
        f.close()
        curr_row = rows - 3
        val = input_to(Get()) 
        if val == 'a' :
            if self._co != 1 :
                self._co -=1
        elif val == 'd':
            if self._co != cols-8 :
                self._co +=1
        for row in range(len(arr)):
            curr_col = self._co
            for col in range(1,cols-1):
                 x._grid[curr_row][col] =  Fore.BLACK + ' '
            for col in range(len(arr[row])-1):
                x._grid[curr_row][curr_col] =  Fore.YELLOW + chr(arr[row][col])
                curr_col +=1
            curr_row +=1


class ball:
    def __init__(self,x):
        val = random.randint(0,6)
        self._x = 40 + val
        self._val = val
        self._y = rows - 4
        self._velox = 0
        self._veloy = 0
        if val == 0 :
            self._velox = -2
            self._veloy = -1
        if val == 1 :
            self._velox = -1
            self._veloy = -1
        if val == 2 :
            self._velox = -1
            self._veloy = -2
        if val == 3 :
            self._velox = 0
            self._veloy = -2
        if val == 4 :
            self._velox = 1
            self._veloy = -2
        if val == 5 :
            self._velox = 1
            self._veloy = -1
        if val == 6 :
            self._velox = 2
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
        if self._y <= 2 :
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
        x._grid[self._y][self._x] = Fore.WHITE + 'o'
        return True


