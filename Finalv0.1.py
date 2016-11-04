import turtle

screen_width = 400
screen_hieght = 400
turtle.setup(screen_width, screen_hieght)
the_turtle = turtle.Turtle()

white = (255,255,255,)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

window = turtle.Screen()
turtle.colormode(255)
window.title("Turtle Graphics Screen")

print("Please enter a starting x and y coordinate")
while True:
    try:
        start_coord = [int(i) for i in input().split(' ')]
        print("Valid Input, Check Turtle Window.")
        break
    except:
        print("Invalid input.")
the_turtle.setposition(start_coord[0],start_coord[1])
the_turtle.penup()

while True:
    print("Please enter an end point x, y coordinate")
    try:
        end_coord = [int(i) for i in input().split(' ')]
        break
    except:
        print("Invalid input")

while True:
    print("Please choose an obstacle type")
    print("S = Rectangle, T = Triangle")
    try:
        ob_type = input()
        break
    except:
        print("Invalid Input")

while True:
    if ob_type.lower() == 's':
        pass
    elif ob_type.lower == 't':
        pass
turtle.exitonclick()