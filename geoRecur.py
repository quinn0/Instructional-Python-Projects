
from turtle import *
from math import *
import random

dim1 = 1000
dim2 = 1000


# screen = Screen()
# screen.setup(width=dim1, height=1500, startx=0, starty=0)
mode("standard")
colormode(255)

setworldcoordinates(0, 0, dim1, dim2)


def stairShrink(step, shrink):
    if step == 0:
        done()
    left(90)
    forward(step)
    right(90)
    forward(step)
    stairShrink(step-step*shrink, shrink)
ht()
speed(0)

# stairShrink(100, .1)
setworldcoordinates(-1*dim1, -1*dim2, dim1, dim2)


def seashell(r, circles):
    if circles == 0:
        done()
    else:
        circle(r)
        seashell(r*.6, circles-1)

# seashell(500, 100)

#centering turtle in next ring
def concentric(r, circles, shrink):
    if circles == 0:
        done()
    else:
        circle(r)
        newR = r - shrink*r
        penup()
        left(90)
        forward(r-newR)
        right(90)
        pendown()
        concentric(newR, circles-1, shrink)

# speed(0)

# concentric(500, 30, .1)



def square(s):
    for i in range(4):
        forward(s)
        left(90)
    
setworldcoordinates(0, 0, dim1, dim2)
def squarecentric(s):
    if(s<1):
        done()
    square(s)
    forward(s/2)
    left(45)
    squarecentric(s*sqrt(2)/2)
# speed(0)
# ht()
# squarecentric(950)

def eqTri(s, shade):
    color(shade,shade,shade)
    begin_fill()
    for i in range(3):   
        forward(s)
        left(120)
    end_fill()
    

# eqTri(800)
# def tricentric(s):
#     if(s<10):
#         done()
#     eqTri(s)
#     forward(s/2)
#     left(60)
#     tricentric(s/2)

# tricentric(1000)


def tricentric2(s, shade):
    if(s<1):
        done()
    if(shade > 255):
        shade = 0
    eqTri(s, shade)
    forward(s/2)
    left(60)
    tricentric2(s/2, shade + 40)

ht()
# tricentric2(1000, 0)

## then they mess around with spiraling

#One of their own that incorporates spiral

def sunSpiral(s, shade):
    if(s<1):
        done()
    if(shade > 255):
        shade = 0
    eqTri(s, shade)
    forward(s/2)
    left(30)
    sunSpiral(s- s*.01, shade + 40)
setworldcoordinates(-1*dim1, -1*dim2, 2*dim1, 2.5*dim2)

sunSpiral(1000, 0)
