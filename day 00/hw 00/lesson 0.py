from turtle import *

shape("turtle")
speed(15)
width(5)
color("blue")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)

color("yellow")
begin_fill()
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 110)
pendown()
color("brown")

right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

penup()
goto(140, 110)
pendown()

right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20) 
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)
penup()
goto(-200, 200)

exitonclick()