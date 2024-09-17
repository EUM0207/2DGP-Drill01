import turtle

screen = turtle.Screen()

turtle.shape('turtle')

move_t = 50

def move_up():
    turtle.setheading(90)
    turtle.forward(move_t)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(move_t)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(move_t)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(move_t)
    turtle.stamp()

def restart():
    turtle.reset()  


screen.listen()  
screen.onkey(move_up, "w")
screen.onkey(move_up, "Up")  
screen.onkey(move_down, "s")
screen.onkey(move_down, "Down")  
screen.onkey(move_left, "a")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "d")
screen.onkey(move_right, "Right")
screen.onkey(restart, "Escape")


turtle.done()
