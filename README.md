# BRICK BREAKER

## Introduction 

It is an arcade game built in Python3(terminal based) inspired form the old classic brick breaker. The player will be using paddle with a bouncing ball to smash a wall of bricks and make high scores !. The objective of the game is to break all the bricks as fast as possible and beat the highest score ! .You loose a life when the ball touches the ground below the paddle.

## Installation
- git clone https://github.com/Dineshg49/brick-game.git
- cd brick-game
- python3 main.py

## OOPS CONCEPTS 

#### Inheritence 
There is one main brick class and different types of bricks which have different colours are inherited from it .

### Polymorphism
All the child classes of the powerup class have functions with same names create() and end().

### Encapsulation 
Class and Object based approach is used for all the functionality implemented 

### Abstraction 
Intitutive Functionality is used where required as for paddle and ball to move() etc.

## Quick - Game Guide 
### Paddle :
- Press 'a' and 'd' to move the paddle horizontally 
- Press 's' to release the ball
### Bricks :
There are 5 different types of bricks :
- 'A' - Bricks with health 1
- '0' - Bricks with health 2
- 'X' - Bricks with health 3
- 'U' - Unbreakable Bricks
- 'L' - Exploding Bricks

### Score and Time :
 - 1 Score is added on every time the ball collides with bricks/disappears in case of exploding brick (except the unbreakable bricks)
 - Time is calculated from the start of the game
 - There are initially 3 lives , you loose a life when ball touches the ground.

 ### Powerups :
 - There are 5 types of powerups which randomly appear when collision with brick . They last for 10 seconds and are lost with a loss of a life 

