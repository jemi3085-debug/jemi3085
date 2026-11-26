import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.pensize(0.6)
t.color("gray")

top = (0, 100)
bottom = (0, -100)
left = (-58, 0)
right = (58, 0)

def line(p1, p2):
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)

line(top, right)
line(right, bottom)
line(bottom, left)
line(left, top)

n = 24

for i in range(n + 1):
    k = i / n

    p1 = (left[0] * (1-k), left[1] * (1-k) + bottom[1] * k)
    p2 = (right[0] * (1-k), right[1] * (1-k) + bottom[1] * k)

    line(top, p1)
    line(top, p2)

    p3 = (left[0] * (1-k), left[1] * (1-k) + top[1] * k)
    p4 = (right[0] * (1-k), right[1] * (1-k) + top[1] * k)

    line(bottom, p3)
    line(bottom, p4)

for a, b in [(115, 20), (90, 12)]:
    t.penup()
    t.goto(-a, 0)
    t.pendown()

    for i in range(361):
        angle = math.radians(i)
        x = a * math.cos(angle)
        y = b * math.sin(angle)
        t.goto(x, y)

t.hideturtle()
turtle.done()