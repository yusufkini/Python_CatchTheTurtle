import turtle as t
from random import randint
import time

turtleScreen = t.Screen()
turtleScreen.setup(1000,1000)
turtleScreen.bgcolor("light blue")
turtleScreen.title("Catch the Turtle")

turtle1 = t.Turtle()
turtle1.hideturtle()
turtle1.color("green")
turtle1.shape("turtle")
turtle1.penup()
turtle1.setheading(90)
turtle1.shapesize(2,2,1)    #Change the size of Turtle, default --> shapesize(width=1,height=1,turtle's outline=1) --> 1 = 20 pixels

scoreObj = t.Turtle()
scoreObj.hideturtle()
scoreObj.penup()
scoreObj.speed(0)
scoreObj.goto(0,430)

timer = t.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 460)

start = time.time()
timeFlag = True
count = 20
catchScore = 0 # How many turtles did you catch?

def catchingTurtles(x,y):
    global catchScore
    catchScore += 1
    turtleCordX = x
    turtleCordY = y

while timeFlag:
    coordinateX = randint(-400, 400)
    coordinateY = randint(-400, 400)
    turtle1.teleport(coordinateX, coordinateY)
    turtle1.showturtle()
    turtle1.onclick(catchingTurtles)
    time.sleep(0.9)

    if (int(time.time() - start) % 2 == 0):
        turtle1.hideturtle()
        turtleScreen.update()

    if (int(time.time() - start)) > 20:
        timeFlag = False
    else:
        timer.clear()
        timer.write(arg=f"Time: {count}", align="center", font=("Arial",18,"normal"))
        scoreObj.clear()
        scoreObj.write(arg=f"Points: {catchScore}", align="center", font=("Arial", 18, "normal"))
        turtleScreen.update()
        count -= 1

    if timeFlag == False:
        timer.clear()
        timer.write(f"Game Over!", align="center",font=("Arial", 18, "normal"))
        turtle1.hideturtle()
        turtleScreen.update()

t.done()
