from colorama import Fore, Back, Style
from global_var import *
from input import *
from collisons import *


class paddle:
    def __init__(self,x):
        self._stick = 0
        self._size = 7
        self._balls = []
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
            for col in range(self._size):
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
            if self._co != 2 :
                self._co -=1
        elif val == 'd':
            if self._co != cols-self._size -2  :
                self._co +=1
        elif val == 's' :
            return False
        elif val == 'f':
            x._lives = 0

        x._grid[bal._y][bal._x] = Fore.BLACK + ' '
        bal._x = bal._val + self._co
        x._grid[bal._y][bal._x] = Fore.WHITE + 'o'
        for row in range(len(arr)):
            curr_col = self._co
            for col in range(1,cols-1):
                 x._grid[curr_row][col] =  Fore.BLACK + ' '
            for col in range(self._size):
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
        elif val == 'f':
            x._lives = 0
        for row in range(len(arr)):
            curr_col = self._co
            for col in range(1,cols-1):
                 x._grid[curr_row][col] =  Fore.BLACK + ' '
            for col in range(self._size):
                x._grid[curr_row][curr_col] =  Fore.YELLOW + chr(arr[row][col])
                curr_col +=1
            curr_row +=1
