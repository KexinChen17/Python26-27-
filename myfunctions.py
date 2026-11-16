import turtle
bob = turtle.Turtle()
bob.speed(0)
def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
def fish(x, y):
    bob.color("orange")
    jump(x - 20, y)
    bob.begin_fill()
    bob.goto(x - 50, y + 20)
    bob.goto(x - 50, y - 20)
    bob.goto(x - 20, y)
    bob.end_fill()

    jump(x, y)
    bob.dot(50, "orange")
def bubble(x, y, size):
    jump(x, y)
    bob.color("blue")
    bob.circle(size)
def seaweed(x, y):
    bob.color("green")
    bob.width(8)

    jump(x, y)
    bob.setheading(80)
    bob.circle(-30, 60)
    bob.circle(30, 60)
    bob.circle(-30, 60)
    
