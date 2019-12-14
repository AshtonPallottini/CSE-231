#####################################################################
# CSE 231 Project Number 2
#
# Algorithm
#   Import turtle and random
#   Prompt for a number of squares to draw
#       If return is zero or negative, halt program 
#   Draw first square as 400x400 and centered at (0,0)
#   Shrink size of each subsequent square by 36
#       All remaining squares are also centered at (0,0)
#####################################################################

import turtle
import random

def pick_color():
    colors = ["blue","black","brown","red","yellow","green",\
    "orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]    

#Prompts for how many squares to draw.
num_squares = input("How many squares do you want:")
#Converts the input from a string to an integer
x = int(num_squares)
#Defines two variables. One for side length and one for start point.
y = 400
z = (200)

if x > 0 :
    while x > 0 :
        #Prevents the turtle from drawing as we move
        turtle.up() 
        #Moves the turtle to where we start drawing each square
        turtle.goto(z, -z)
        
        #Picks a random color for each square drawn
        random_color = pick_color()
        print(random_color)
        turtle.color(random_color)
        
        #Draws the squares and fills them with the random color
        turtle.down()
        turtle.begin_fill()
        turtle.right(180)
        turtle.forward(y)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(90)
        turtle.forward(y)
        turtle.right(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.end_fill()
       
        x -= 1 #Subtracts one from how many squares we need to draw
        y -= 36 #Subtracts 36 from the next square's side length
        z -= 18 #Moves the next starting spot for drawing

else :
    print( "That is invalid. Positives only.")    
    
    
    
    
#Questions
#Q1:6
#Q2:2
#Q3:2
#Q4:6