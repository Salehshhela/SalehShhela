import turtle

t = turtle.Turtle()
t.speed(1)  
t.color("blue")  
t.pensize(3)  

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(200, 200)
t.pendown()

t.circle(50)

t.penup()
t.goto(-200, 200)
t.pendown()

t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-200, -200)
t.pendown()

t.color("green")
for i in range(50):
    t.forward(i)
    t.left(90)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("yellow")
for i in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

t.penup()
t.goto(200, -200)
t.pendown()
t.color("purple")
for i in range(6):
    t.forward(80)
    t.left(60)

t.penup()
t.goto(-100, -200)
t.pendown()
t.color("red")
t.begin_fill()
t.left(45)
t.forward(70)
t.left(90)
t.forward(70)
t.left(90)
t.forward(70)
t.left(90)
t.forward(70)
t.left(135)
t.end_fill()

t.penup()
t.goto(150, -200)
t.pendown()
t.color("#FF9900")  # Orange
t.begin_fill()
t.circle(70)
t.end_fill()
t.penup()
t.goto(120, -250)
t.pendown()
t.color("black")
t.circle(15)
t.penup()
t.goto(180, -250)
t.pendown()
t.circle(15)
t.penup()
t.goto(150, -170)
t.pendown()
t.forward(70)

turtle.done()