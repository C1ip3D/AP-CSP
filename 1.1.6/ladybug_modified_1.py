import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.setheading(0)  # Ensure turtle starts facing right
ladybug.pensize(40)
ladybug.circle(5)

num_legs = 6
leg_length = 55
angle = 60 / (num_legs/2)  
current_leg = 0


while (current_leg < num_legs):
    ladybug.penup()
    ladybug.pensize(5)
    ladybug.goto(0,-40)
    ladybug.pendown()
    if current_leg < 3:
        ladybug.setheading(150 + angle*current_leg)
    else:
        ladybug.setheading(angle*(current_leg-3) - 20)
    ladybug.forward(leg_length)
    current_leg = current_leg + 1

# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()