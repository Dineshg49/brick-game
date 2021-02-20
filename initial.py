import time
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
            for i in bal._power:
              powerup.move(i,x,pad,bal)
              powerup.end(i,x,pad,bal)
            static_bg.print_grid(x)
            pad.move(x)
            if over == False:
              x._lives -= 1
              over = True
              pad = paddle(x)
              bal = ball(x)
              chec = True
            time.sleep(0.1)


