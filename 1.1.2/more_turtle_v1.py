# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(100)

painter.penup()
# move the turtle to another part of the screen
painter.goto(300, 100)
painter.pendown()

# add code here for an arc
painter.circle(100, 240)

painter.penup()
# move the turtle to another part of the screen
painter.goto(-300, 100)
painter.pendown()

# add code here for an arc that is greater than 
#90 degrees and has 5 steps
painter.circle(100, 270, 5)

painter.penup()
# move the turtle to another part of the screen
painter.goto(0, -200)
painter.pendown()

# add code here to create a polygon of your choice
# using the circle method
painter.circle(100, 360, 5)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()