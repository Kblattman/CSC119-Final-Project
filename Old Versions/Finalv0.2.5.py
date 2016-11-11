import turtle

screen_width = 400
screen_height = 400
turtle.setup(screen_width, screen_height) # Initilize Screen

turtle.colormode(255) # Use the 0-255 RGB Color system
white = (255,255,255) # Define Common Color RBG Values
black = (0,0,0)       # As Tuples for compatibility with
red = (255,0,0)       # Turtle class functions.
green = (0,255,0)
blue = (0,0,255)

shape_turtle = turtle.Turtle() # Create the Shape Turtle to be used for drawing shapes
shape_turtle.ht()              # Hide the Shape Turtle
shape_turtle.pu()              # Pull the pen up

the_turtle = turtle.Turtle() # Create the Turtle object literally as the_turtle
the_turtle.setpos(0,0)       # .setposition can be shortend
                             ## the_turtle.ht() ## Hide the Turtle for pixel perfect movement.
window = turtle.Screen()     # Create the screen object as window var
window.title("Turtle Maze Final v0.2.5")

###DECLARE ALL GLOBAL VARIABLE INITILIZATIONS ABOVE THIS LINE ###
class Move:
    '''
    Each Function Moves the_turtle used for event handeling
    '''
    def forwards():
        the_turtle.fd(2)  # One pixel is too slow 2 might also be.
    def backwards():
        the_turtle.bd(2)  # All these functions are shortend
    def left():
        the_turtle.lt(15) # 15 degree turning angles
    def right():
        the_turtle.rt(15)
        
def draw_shape(x, y):
    '''
    On mouse click takes the xy of mouse and draws a shape
    with the xy being the upper left of the object
    '''
    shape_type = window.textinput('Shapes', 'Enter a shape type. EX: square, triangle, circle')
    print('draw shape at {},{}'.format(x,y)) # For proof of concept
    if shape_type.lower() == 'square':
        pass # Draw a square
    elif shape_type.lower() == 'triangle':
        pass # Draw a triangle
    elif shape_type.lower() == 'circle':
        shape_turtle.setpos(x, y)
        shape_turtle.pd()
        shape_turtle.circle(20)
        shape_turtle.pu()
        pass # Draw a circle
    
### DECLARE ALL FUNCTIONS ABOVE THIS LINE ###
                                                    # Empty Space
### USER INPUT ###
while True:
    start_pos = []
    try:
        # This is a very long line... but it works lol.
        start_pos = [int(i) for i in
                     window.textinput('Start', 'Enter a starting position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                         int(-screen_width/2),int(screen_width/2),int(-screen_height/2),int(screen_height/2))).split(' ') ]
    except:
        pass
    if len(start_pos) == 2:
        # Ensure player starting position input is within the screen boundary
        if start_pos[0] > int(-screen_width/2) and start_pos[0] < int(screen_width/2):
            if start_pos[1] > int(-screen_height/2) and start_pos[1] < int(screen_height/2):
                break
            else:
                pass
        else:
            pass
        
# Put the_turtle at the user input position.            
the_turtle.pu() # Pull Pen Up to Prevent drawing
the_turtle.setpos(start_pos[0],start_pos[1]) # Go to the user x y coord
the_turtle.pd() # Pull Pen Down

while True:
    end_pos = []
    try:
        # Another long line...
        end_pos = [int(i) for i in
                   window.textinput('End', 'Enter a destination position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                       int(-screen_width/2),int(screen_width/2),int(-screen_height/2),int(screen_height/2))).split(' ')]
    except:
        pass
    if len(end_pos) == 2:
        # Ensure player end position input is within the screen boundary
        if end_pos[0] > int(-screen_width/2) and end_pos[0] < int(screen_width/2):
            if end_pos[1] > int(-screen_height/2) and start_pos[1] < int(screen_height/2):
                break
            else:
                pass
        else:
            pass
    
### BEGIN EVENT HANDELING ###
window.onkeypress(Move.forwards, 'Up')
window.onkeypress(Move.backwards, 'Down')
window.onkeypress(Move.left, 'Left')
window.onkeypress(Move.right, 'Right')
window.onclick(draw_shape)

window.listen()
### END EVENT HANDELING : MUST BE LAST SECTION OF PROGRAM ###
