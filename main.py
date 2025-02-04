import turtle as t
import random as r
s = t.Screen()
t = t.Turtle()
s.setup(500, 500)
t.hideturtle()
t.penup()
t.goto(-250, -50)
t.pendown()
t.speed(0)
distance = 100
rand = r.randint(1, 6)
print(rand)
def dice():
    global distance
    for j in range(3):
        for i in range(4):
            t.forward(100)
            t.left(90)
        if rand == 1 or rand == 3 or rand == 5:
            t.penup()
            t.goto((0 - distance),0)
            t.pendown()
            t.dot(10)
        if rand == 2 or rand == 6 or rand == 4 or rand == 5 or rand == 3:
            t.penup()
            t.goto(25 - distance,25)
            t.pendown()
            t.dot(10)
            t.penup()
            t.goto(-25 - distance, -25)
            t.pendown()
            t.dot(10)
        if rand == 4 or rand == 5 or rand == 6:
            t.penup()
            t.goto(25 - distance,-25)
            t.pendown()
            t.dot(10)
            t.penup()
            t.goto(-25 - distance, 25)
            t.pendown()
            t.dot(10)
        if rand == 6:
            t.penup()
            t.goto(25 - distance,0)
            t.pendown()
            t.dot(10)
            t.penup()
            t.goto(-25 - distance, 0)
            t.pendown()
            t.dot(10)
        distance += 100
        t.penup()
        t.goto(distance - 100, -50)
dice()
s.mainloop()
