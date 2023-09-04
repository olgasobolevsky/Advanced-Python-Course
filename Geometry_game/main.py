import turtle

# create a canvas instance
my_turtle = turtle.Turtle()

my_turtle.penup()  # don't touch the canvas with the pen
my_turtle.goto(50, 75)  # go to certain coordinate

my_turtle.pendown()  # touch the canvas with the pen
my_turtle.forward(100)  # move forward 100 pixels
my_turtle.left(90)  # turn left 90 degrees
my_turtle.forward(200)  # move forward 200 pixels
my_turtle.left(90)  # turn left 90 degrees
my_turtle.forward(100)  # move forward 100 pixels
my_turtle.left(90)  # turn left 90 degrees
my_turtle.forward(200)  # move forward 200 pixels

turtle.done()
