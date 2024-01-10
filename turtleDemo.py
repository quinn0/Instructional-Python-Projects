###   turtleDemo  ###

## Below I will be demonstrating
## the essentials needed 
## to draw with the turtle library
## If interested in all that turtle has to offer
# See: 
# https://docs.python.org/3/library/turtle.html#module-turtle

## Run the code as you read about them in
## In the assignment document and *These Comments*

## The purpose of this example code is to see
## how you can draw the basics using turtle commands
##   While incorporating some recursive elements!

## I suggest keeping this file open and copy-pasting 
## what you need for the assignment. 
##       (Programming isn't about remembering special functions!)

from turtle import * ## Turtle Library 
## Two other functions we'll use for 
## Demonstration and your assignment (hint)
from math import sqrt 
from random import randint

# Dimensions of our screen. 
# Change these around to suit your purposes!
dim1 = 1000
dim2 = 1000


## mode("standard") sets up a few things we need:
# 1) The direction our turtle faces (the 'heading') to begin drawing
        #Standard ->  Facing East/Right at 0 degrees
# 2) Writing Angles: Degrees Vs Radians 
        #Standard -> Degrees (used for turning)
        ###Example: left(90) rotates turtle 90 degrees 
        #                                   counter-clockwise
# 3) How direction/heading of the turtle is represented
        #Standard -> East: 0 North: 90 West: 180 South: 270 

mode("standard")


# colormode() may be useful to you depending on how creative you get!
# We will use 0-255 here to express the brightness-intensity 
# of the red, green, and blue of a color. 
# Three values together express a color where 
#                         (0,0,0) is black and (255,255,255) is white
colormode(255)

##setworldcoordinates(lowerLeftX, lowerLeftY, upperLeftX, upperLeftY)
## allows us to set the cordinates on the screen
## where the first two arguments are the (x,y) cordinates of
## the lower left corner and the second two are (x,y) coords of
## the upper right corner. The default is (0,0) in the center but,
## depending on how you're drawing something 
#                               you may want to change that!

setworldcoordinates(0, 0, dim1, dim2)

###DRAWING###
# Imagine a pen... but that pen is a turtle.
# shape("turtle")
# # #(you can alseo hide the turtle completely with):
# #             #hideturtle() or ht()
# # When you originally run a turtle program
# # the pen will start down, but you will not always want to draw 
# #command:
# pendown()
# # if turtle moves something is drawn (because pen is down)
# forward(100) #100 is the number of pixels to travel

# #We can rotate the turtle to make a corner:
# left(90) #turn left 90 degrees (now facing North)
# fd(100) ##fd and forward are the same method! lazy fingers

# #lets move the turtle without drawing 
# penup()

# right(90)
# fd(100) 
# right(90) ##Vibe Check: Which direction is turtle facing now?

# ##draw again
# pendown()
# fd(100)

# #done() needs to be called so we can pause the program
# # If we don't do that the window will disappear once 
# # the code finishes running!
# # (exit when finished)
# done()

#Now lets add some recursion
#Examine this function and run the function call below 
# randomWalk(n) will move the turtle n steps
# if a random number is even, it turns left before moving/drawing
# otherwise it turns right and draws

# For visibility reasons, lets change the coordinates back such that
# (0,0) is the center of the screen (who knows where we'll go!)

setworldcoordinates(-1*dim1, -1*dim2, dim1, dim2)
def randomWalk(steps):
    temp = randint(0, 10000) ##makes a random number between 0 and 10000
    if(steps == 0):#Here's our base case (when turtle has taken all of its steps)
        done() # We usually return or print something here
               # In turtle done() pauses the program so think of it
               # as Turtle's return
    elif temp % 2 == 0: 
        left(60) #counter clockwise
    else:
        right(60) #clockwise
    forward(20)
    
    randomWalk(steps - 1) #recursive call reducing steps

## ATTENTION: Comment out LN 65-94 code (highlight + ctr + /)
# BEFORE CONFINUING!
speed(0) ##This makes turtle draw faster!

# #****
# randomWalk(600)
# #****

ht() ## We'll hide the turtle icon for remaining examples
setworldcoordinates(0, 0, dim1, dim2)

## Helper functions can make a complicated procedure really simple
## Let's make some stairs by making a step (upside-down L)
## where size is the length of the side of each step
def step(size):
    left(90) #facing North
    forward(size) #draw up
    right(90) #facing east
    forward(size) #draw right

#then we can make as many stairs as we want 
## lets make some 'shrinking stairs'
## where each step is some fraction, 'shrink', less than the last

def stairShrink(size, shrink):
    if(size < 1): 
        done()    # here size is a counter and modifies the step size!
    else:
        step(size) #makes one step 
        stairShrink(size -  size*shrink, shrink) #the 'new' step size is size -  size*shrink the last

# #****
# stairShrink(400, .5)
# #****


## FOR SEASHELL AND CONCENTRIC FUNCTIONS: THE circle() METHOD
#I strongly recommend making these with the turtle in the center of the screen:
setworldcoordinates(-1*dim1, -1*dim2, dim1, dim2)
##As you might have guessed:
# circle(r) takes a radius, r and draws... a circle of radius, r, pixels
## HOWEVER: Take special note of where turtle starts drawing 
### the pen starts drawing 'r' units south of the center of the circle
### we also start facing east.

# #****
# st()
# speed(1)
# circle(100)
# done()
# #****

### FOR TRICENTRIC2 AND YOUR 
### BEAUTIFUL RECURSIVE GEOMETRIC MASTERPIECE: Filling/Shading in a shape!

# #****
r = 150 #red value
g = 0   #green value
b = 100 #blue value

color(r,g,b) #sets the pen's color to some purple color

ht()
speed(1)

begin_fill()#start
circle(500) #Makes whatever region drawn purple
end_fill() #stop's filling in regions

r += 100 
g += 100
b += 100

color(r,g,b) ##Changed to pink!

begin_fill()
circle(300)
end_fill()

done()

# #****

####Again, feel free to explore other turtle graphics methods to enhance your art!