import turtle as trtl

painter = trtl.Turtle()

for i in range(4):
    painter.forward(100)
    painter.left(90)

wn = trtl.Screen()
wn.mainloop()