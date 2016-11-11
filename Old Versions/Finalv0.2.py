import turtle

screen_width = 400
screen_hieght = 400
turtle.setup(screen_width, screen_hieght) # Initilize Screen

turtle.colormode(255) # Use the 0-255 RGB Color system
white = (255,255,255) # Define Common Color RBG Values
black = (0,0,0)       # As Tuples for compatibility with
red = (255,0,0)       # Turtle class functions.
green = (0,255,0)
blue = (0,0,255)

the_turtle = turtle.Turtle() # Create the Turtle object literally as the_turtle
the_turtle.setpos(0,0)       # .setposition can be shortend
                             ## the_turtle.ht() ## Hide the Turtle for pixel perfect movement.
window = turtle.Screen()     # Create the screen object as window var
window.title("Turtle Maze Final v0.2")
###DECLARE ALL GLOBAL VARIABLE INITILIZATIONS ABOVE THIS LINE ###
class Move:
    '''
    Each Function Moves the_turtle used for event handeling
    '''
    def forwards():
        the_turtle.fd(2)  # One pixel is too slow 2 might also be.
    def backwards():
        the_turtle.bd(2)  # All these fucntions are shortend
    def left():
        the_turtle.lt(15) # 15 degree turning angles
    def right():
        the_turtle.rt(15)
        
def draw_shape(x, y):
    '''
    On mouse click takes the xy of mouse and draws a shape
    with the xy being the upper left of the object
    '''
    shape_type = window.textinput('Shapes', 'Enter a shape type ex. square,triangle')
    print('draw shape at {},{}'.format(x,y)) # For proof of concept
    if shape_type.lower() == 'square'
        pass # Draw a square
    elif shape_type.lower() == 'triangle'
        pass # Draw a triangle
    elif shape_type.lower() == 'circle'
        pass # Draw a circle
    
### DECLARE ALL FUNCTIONS ABOVE THIS LINE ###
                                                    # Empty Space
### USER INPUT ###
start_pos = [int(i) for i in
             window.textinput('Start', 'Enter a starting position: x y').split(' ') ]
the_turtle.pu() # Pull Pen Up to Prevent drawing
the_turtle.setpos(start_pos[0],start_pos[1]) # Go to the user x y coord
the_turtle.pd() # Pull Pen Down
end_pos = [int(i) for i in
           window.textinput('End', 'Enter a destination position: x y').split(' ')]

### BEGIN EVENT HANDELING ###
window.onkeypress(Move.forwards, 'Up')
window.onkeypress(Move.backwards, 'Down')
window.onkeypress(Move.left, 'Left')
window.onkeypress(Move.right, 'Right')
window.onclick(draw_shape)

window.listen()
### END EVENT HANDELING : MUST BE LAST SECTION OF PROGRAM ###


## ALL COMMENT LINES BELOW TO BE DELETED UPON REVIEW ###
##print("Please enter a starting x and y coordinate")
##while True:
##    try:
##        start_coord = [int(i) for i in input().split(' ')]
##        print("Valid Input, Check Turtle Window.")
##        break
##    except:
##        print("Invalid input.")
##the_turtle.setposition(start_coord[0],start_coord[1])
##the_turtle.penup()
##
##while True:
##    print("Please enter an end point x, y coordinate")
##    try:
##        end_coord = [int(i) for i in input().split(' ')]
##        break
##    except:
##        print("Invalid input")
##
##while True:
##    print("Please choose an obstacle type")
##    print("S = Rectangle, T = Triangle")
##    try:
##        ob_type = input()
##        break
##    except:
##        print("Invalid Input")
##
##while True:
##    if ob_type.lower() == 's':
##        pass
##    elif ob_type.lower == 't':
##        pass
## END NESSECARY DELETION ###
