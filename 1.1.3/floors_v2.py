#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
  rem = floor % 21
  rem1 = floor % 6
  if (rem == 0):
    x= x + 50
    y= -150
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
  # set placement and color of turtle
  else: 
    painter.penup()
    painter.goto(x, y)
    y = y + 5 # location of next floor
    painter.color("black")
    if(rem1 > 2):
      painter.color("gray")
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()