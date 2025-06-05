from turtle import *
from random import *

speed(100)
colormode(255)
colors = ["red", "green", "blue"]

def z(side, color):
    pencolor(color)
    for i in range(5):
        forward(side)
        left(145)

def square(side, color):
    pencolor(color)
    for i in range(4):
        fd(side)
        lt(90)



for i in range(1, 1000, 4):
    z(i, choice(colors))


#for i in range(1, 1000, 4):
    #square(i, choice(colors))

done()
