# CODE TO COPY
#   a116_spider.py
import turtle as trtl

spider = trtl.Turtle()
spider.speed(9)

angle = 320
reverse_angle = 140
num_legs= 0
leg_length = 150
spider.pensize(5)
while (num_legs<= 7):
  if (num_legs<= 3):
    spider.penup()
    spider.goto(10, -45)
    spider.pendown()
    spider.setheading(angle/1.5)
    spider.circle(80,-140,10)
    angle = angle + 30
    num_legs= num_legs+ 1
  if (num_legs> 3):
    spider.penup()
    spider.goto(10, -45)
    spider.pendown()
    spider.setheading(reverse_angle/1.5)
    spider.circle(80,140,10)
    reverse_angle = reverse_angle + 30
    num_legs= num_legs+ 1

# Spider Body
spider.fillcolor("black")
spider.begin_fill()
spider.penup()
spider.goto(-30, -55) 
spider.color("black")
spider.pendown()
spider.pensize(40)
spider.circle(40)
spider.setheading(270)
spider.end_fill()
spider.penup()

spider.pencolor('thistle')
#Eye function
def draw_eye():
    spider.pensize(7)
    spider.pendown()
    spider.circle(5)

#Eye 1
spider.goto(-10,-55)
draw_eye()
#Eye 2
spider.penup()
spider.goto(10,-55)
draw_eye()


spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()