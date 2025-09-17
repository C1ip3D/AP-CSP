import turtle as trtl
brush = trtl.Turtle()
brush.pensize(40)
brush.circle(20)
num_legs = 6
leg_length = 70
angle = 380 / num_legs
brush.pensize(5)
current_leg = 0
while (current_leg < num_legs):
  brush.goto(0,0)
  brush.setheading(angle*current_leg)
  brush.forward(leg_length)
  current_leg = current_leg + 1
brush.hideturtle()
wn = trtl.Screen()
wn.mainloop()