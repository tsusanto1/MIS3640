import turtle
import math
jerry = turtle.Turtle()

def shapeOne(t, r):
    t.pensize(2)
    t.ht()
    t.circle(r)
    t.penup()
    t.sety(r)
    t.pendown()
    t.rt(30)
    for i in range(4):
        t.fd(r)
        t.lt(120)
        t.fd(r)
        t.lt(120)
        t.fd(r)
        t.rt(150)
    for i in range(4):
        t.penup()
        t.fd(r/2)
        t.pendown()
        t.circle(r*(math.sqrt(3)/6))
        t.penup()
        t.goto(0,r)
        t.lt(90)
        t.pendown()

shapeOne(jerry, 150)

def shapeTwo(t,r):
    t.ht()
    t.circle(r)
    t.penup()
    t.sety(r)
    t.pendown()
    for i in range(6):
        t.circle(r,60)
        t.lt(120)
        t.circle(r,60)
        t.lt(60)

#shapeTwo(jerry,150)

def shapeThree(t,r):
    t.pensize(5)
    t.ht()
    t.circle(r)
    t.penup()
    t.sety(r)
    t.pendown()
    t.circle(r*0.5, 180)
    t.penup()
    t.sety(r)
    t.pendown()
    t.circle(r*0.5, 180)
    t.penup()
    t.sety((r*0.5)-(r/6))
    t.pendown()
    t.circle(r/6)
    t.penup()
    t.sety((r*1.5)-(r/6))
    t.pendown()
    t.circle(r/6)

#shapeThree(jerry, 150)


print(jerry)
turtle.mainloop()

