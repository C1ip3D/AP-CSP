#Init
import turtle as trtl
brush = trtl.Turtle()
# Spider Torso
brush.pensize(40)
brush.circle(20)
#Leg attributes of spider
num_legs = 8
leg_length = 70
angle = 360 / num_legs
brush.pensize(5)
current_leg = 0
# Draw Legs
while (current_leg < num_legs):
  brush.goto(0,20)
  brush.setheading(angle*current_leg)
  brush.forward(leg_length)
  current_leg = current_leg + 1
# Cleanup
brush.hideturtle()
wn = trtl.Screen()
wn.mainloop()