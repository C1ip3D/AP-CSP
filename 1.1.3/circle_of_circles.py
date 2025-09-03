#   a113_circle_of_circles.py
#   Modify this code to draw a circle of circles
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")

for i in range(1, 19):
    painter.forward(20)
    painter.right(20)
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()