#Init
import turtle as trtl

def draw_eye():
    brush.pensize(7)
    brush.pendown()
    brush.circle(5)
    
brush = trtl.Turtle()

# Spider Torso
brush.pensize(40)
brush.circle(20)
#Leg attributes of spider
num_legs = 8
leg_length = 70
angle = 120 / (num_legs/2)
brush.pensize(5)
current_leg = 0
# Draw Legs
while (current_leg < num_legs):
  brush.goto(0,20)
  if current_leg < 4:
    brush.setheading(angle*current_leg - 60)
  else:
    brush.setheading(angle*(current_leg-4) + 120)
  brush.forward(leg_length)
  current_leg = current_leg + 1

brush.penup()
#Spider Eyes
brush.pencolor('white')

#Eye 1
brush.goto(-17,30)
draw_eye()
#Eye 2
brush.penup()
brush.goto(17,30)
draw_eye()
# Cleanup
brush.hideturtle()
wn = trtl.Screen()
wn.mainloop()