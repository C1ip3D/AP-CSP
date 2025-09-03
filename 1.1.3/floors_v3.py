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
    
    # Three-color pattern every three floors
    if rem1 == 0 or rem1 == 1:
      painter.color("black")
    elif rem1 == 2 or rem1 == 3:
      painter.color("gray")
    else:  # rem1 == 4 or rem1 == 5
      painter.color("red")
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()