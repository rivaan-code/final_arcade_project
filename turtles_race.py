import turtle
import time
import random

#window setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE", font=("Arial",30,"bold"))
turtle.penup()

#DIRT
turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(800)
turtle.end_fill()

#start line
turtle.color("black")
turtle.up()
turtle.setposition(-200,-100)
turtle.write('Start line',align='center')
turtle.right(90)
turtle.forward(10)
turtle.down()
turtle.forward(250)

#Finish line
turtle.up()
turtle.setposition(210,-100)
turtle.write('Finish line',align='center')
turtle.forward(10)
turtle.down()
turtle.forward(250)
turtle.hideturtle()

#Turtle 1
def draw_turtle(color,x,y):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.shape('turtle')
    t.penup()
    t.goto(x,y)
    t.pendown()
    return t

t1 = draw_turtle("red", -230,100)
t2 = draw_turtle("blue", -230,50)
t3 = draw_turtle("purple", -230,0)
t4 = draw_turtle("magenta", -230, -50)

time.sleep(1)

#move the turtles
for i in range(145):
    t1.forward(random.randint(1,5))
    t2.forward(random.randint(1,5))
    t3.forward(random.randint(1,5))
    t4.forward(random.randint(1,5))

turtle.done()