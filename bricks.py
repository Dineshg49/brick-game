from colorama import Fore, Back, Style
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
                    brick1.create(x,curr_row,curr_col)
                elif ch == '0':
                    brick2.create(x,curr_row,curr_col)
                elif ch == 'A':
                    brick3.create(x,curr_row,curr_col)
                elif ch == 'U':
                    brick4.create(x,curr_row,curr_col)
                elif ch == 'L':
                    brick5.create(x,curr_row,curr_col)
                curr_col +=1
            curr_row +=1
    
class brick1(bricks):
    def create(x,curr_row,curr_col):
        x._grid[curr_row][curr_col] =  Fore.RED + 'X'

class brick2(bricks):
    def create(x,curr_row,curr_col):
        x._grid[curr_row][curr_col] =  Fore.YELLOW + '0'

class brick3(bricks):
    def create(x,curr_row,curr_col):
        x._grid[curr_row][curr_col] =  Fore.GREEN + 'A'

class brick4(bricks):
    def create(x,curr_row,curr_col):
        x._grid[curr_row][curr_col] =  Fore.LIGHTCYAN_EX + 'U'

class brick5(bricks):
    def create(x,curr_row,curr_col):
        x._grid[curr_row][curr_col] = Fore.CYAN + 'L'
