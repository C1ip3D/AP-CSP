import turtle as trtl

painter = trtl.Turtle()

# Inputs
head_radius = int(input("Enter the radius of the head: "))
torso_length = int(input("Enter the length of the torso: "))
arm_length = int(input("Enter the length of the arms: "))
leg_length = int(input("Enter the length of the legs: "))

head_color = input("Enter the color of the head: ")
torso_color = input("Enter the color of the torso: ")
arm_color = input("Enter the color of the arms: ")
leg_color = input("Enter the color of the legs: ")

# Setup
painter.penup()
painter.goto(0,100)

#Draw Head
painter.pendown()
painter.color(head_color)
painter.circle(head_radius)

#Upper Torso
painter.setheading(-90)
painter.color(torso_color)
painter.forward(torso_length/4)

#Save current coords
torso_x, torso_y = painter.pos()

#Lower Torso
painter.forward(3*(torso_length/4))


# Save current coords
leg_x, leg_y = painter.pos()

#Left Leg
painter.color(leg_color)
painter.right(30)
painter.forward(leg_length)

# Reposition and draw right leg

painter.goto(leg_x, leg_y)
painter.setheading(-90)
painter.left(30)
painter.forward(leg_length)

#Reposition and draw left arm
painter.penup()
painter.goto(torso_x, torso_y)
painter.pendown()
painter.color(arm_color)
painter.setheading(-90)
painter.right(45)
painter.forward(80)


# Reposition and draw right arm

painter.penup()
painter.goto(torso_x, torso_y)
painter.pendown()
painter.setheading(-90)
painter.left(45)
painter.forward(80)


wn = trtl.Screen()
wn.mainloop()
