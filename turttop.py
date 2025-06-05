from turtle import *
colormode(255)
bgcolor("medium violet red")
speed(100)
pensize(3)

for i in range(360):
    pencolor(i % 90, 0, i % 90)
    rt(1)
    fd(100)
    bk(100)

done()