import turtle

turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(1)
colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple"]
for i in range(90):
    turtle.pencolor(colors[i % 7])
    turtle.circle(100)
    turtle.left(2)
    turtle.circle(100)
    turtle.left(2)
turtle.hideturtle()
turtle.done()
