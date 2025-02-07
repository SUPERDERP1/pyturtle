import turtle
import random as r
s = turtle.Screen()
t = turtle.Turtle()
s.setup(500, 500)
t.hideturtle()
t.penup()
t.goto(-50, -50)
t.pendown()
t.speed(0)
d1lock = False
d2lock = False
d3lock = False
enabled = False
p1score = 0
p2score = 0
turn = 0
roundCount = 0
def score():
    global d1lock, d2lock, d3lock, rand1, rand2, rand3, p1score, p2score, turn, roundCount
    if turn == 0:
        turn = 1
        p1score += rand1 + rand2 + rand3
        print(p1score)
        t.goto(0, 100)
        t.write("Player 1 Score: " + str(p1score), align="center", font=("Arial", 20, "bold"))
        t.goto(0, -100)
        t.write("Player 2 Score: " + str(p2score), align="center", font=("Arial", 20, "bold"))
    elif turn == 1:
        roundCount += 1
        turn = 0
        p2score += rand1 + rand2 + rand3
        print(p2score)
        t.goto(0, 100)
        t.write("Player 1 Score: " + str(p1score), align="center", font=("Arial", 20, "bold"))
        t.goto(0,-100)
        t.write("Player 2 Score: " + str(p2score), align="center", font=("Arial", 20, "bold"))
    d1lock = False
    d2lock = False
    d3lock = False
def d1():
    global d1lock, enabled
    global d2lock
    global d3lock
    global rand1
    enabled = True
    if d1lock == True & d2lock == True & d3lock == True:
        score()
    if not d1lock:
        rand1 = r.randint(1, 6)
        print(rand1)
    t.goto(-50, -50)
    for i in range(4):
        t.pendown()
        t.forward(100)
        t.left(90)
    if rand1 == 1 or rand1 == 3 or rand1 == 5:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.dot(10)
    if rand1 == 2 or rand1 == 6 or rand1 == 4 or rand1 == 5 or rand1 == 3:
        t.penup()
        t.goto(25, 25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-25, -25)
        t.pendown()
        t.dot(10)
    if rand1 == 4 or rand1 == 5 or rand1 == 6:
        t.penup()
        t.goto(25, -25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-25, 25)
        t.pendown()
        t.dot(10)
    if rand1 == 6:
        t.penup()
        t.goto(25, 0)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-25, 0)
        t.pendown()
        t.dot(10)
    t.penup()
    t.goto(0, 100)
    t.write("Player 1 Score: " + str(p1score), align="center", font=("Arial", 20, "bold"))
    t.goto(0, -100)
    t.write("Player 2 Score: " + str(p2score), align="center", font=("Arial", 20, "bold"))
def d3():
    global d3lock, rand3, enabled
    if not d3lock:
        rand3 = r.randint(1, 6)
        print(rand3)
    t.goto(75, -50)
    for i in range(4):
        t.pendown()
        t.forward(100)
        t.left(90)
    if rand3 == 1 or rand3 == 3 or rand3 == 5:
        t.penup()
        t.goto(125, 0)
        t.pendown()
        t.dot(10)
    if rand3 == 2 or rand3 == 6 or rand3 == 4 or rand3 == 5 or rand3 == 3:
        t.penup()
        t.goto(150, 25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(100, -25)
        t.pendown()
        t.dot(10)
    if rand3 == 4 or rand3 == 5 or rand3 == 6:
        t.penup()
        t.goto(150, -25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(100, 25)
        t.pendown()
        t.dot(10)
    if rand3 == 6:
        t.penup()
        t.goto(100, 0)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(150, 0)
        t.pendown()
        t.dot(10)
    t.penup()
    t.goto(0, 100)
    t.write("Player 1 Score: " + str(p1score), align="center", font=("Arial", 20, "bold"))
    t.goto(0, -100)
    t.write("Player 2 Score: " + str(p2score), align="center", font=("Arial", 20, "bold"))
    enabled = False
def d2():
    global d2lock, rand2
    if not d2lock:
        rand2 = r.randint(1, 6)
        print(rand2)
    t.goto(-175, -50)
    for i in range(4):
        t.pendown()
        t.forward(100)
        t.left(90)
    if rand2 == 1 or rand2 == 3 or rand2 == 5:
        t.penup()
        t.goto(-125, 0)
        t.pendown()
        t.dot(10)
    if rand2 == 2 or rand2 == 6 or rand2 == 4 or rand2 == 5 or rand2 == 3:
        t.penup()
        t.goto(-100, 25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-150, -25)
        t.pendown()
        t.dot(10)
    if rand2 == 4 or rand2 == 5 or rand2 == 6:
        t.penup()
        t.goto(-100, -25)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-150, 25)
        t.pendown()
        t.dot(10)
    if rand2 == 6:
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.dot(10)
        t.penup()
        t.goto(-150, 0)
        t.pendown()
        t.dot(10)
    t.penup()
    t.goto(0, 100)
    t.write("Player 1 Score: " + str(p1score), align="center", font=("Arial", 20, "bold"))
    t.goto(0, -100)
    t.write("Player 2 Score: " + str(p2score), align="center", font=("Arial", 20, "bold"))
def click(x,y):

    global d1lock
    global d2lock
    global d3lock
    print(x,y)
    if enabled == False:
        if x < 50 and y < 50 and x > -50 and y > -50 and d1lock == False:
            print("d1 Clicked")
            d1lock = True
            t.clear()
            d1()
            d2()
            d3()
        elif x < -75 and y < 50 and x > -175 and y > -50 and d2lock == False:
            print("d2 Clicked")
            d2lock = True
            t.clear()
            d1()
            d2()
            d3()
        elif x < 175 and y < 50 and x > 75 and y > -50 and d3lock == False:
            print("d3 Clicked")
            d3lock = True
            t.clear()
            d1()
            d2()
            d3()
d1()
d2()
d3()
turtle.onscreenclick(click)
s.mainloop()
