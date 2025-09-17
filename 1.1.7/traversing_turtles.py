#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

my_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle()
    t.shape(s)
    new_color = turtle_colors.pop()
    t.pencolor(new_color)
    t.fillcolor(new_color)
    t.pensize(20)
    my_turtles.append(t)

startx = 0
starty = 0
direction = 0

for i in range(5):
    for t in my_turtles:
        t.setheading(direction)
        t.penup()
        t.goto(startx, starty)
        t.pendown()
        t.right(55)

        t.forward(60 + i*20)

        direction = direction + 45
        startx = t.xcor()
        starty = t.ycor()

        if i == 0:
            direction = direction + 5

wn = trtl.Screen()
wn.mainloop()