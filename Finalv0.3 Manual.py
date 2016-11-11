import turtle
import time

SCRN_WIDTH = 400        # Constant for the screen width in pixels
SCRN_HEIGHT = 400       # Screen Height in pixels
turtle.setup(SCRN_WIDTH, SCRN_HEIGHT) # Initilize Screen
turtle.colormode(255)   # Use the 0-255 RGB Color system
white = (255,255,255)   # Define Common Color RBG Values
black = (0,0,0)         # As Tuples for compatibility with
red = (255,0,0)         # Turtle class functions.
green = (0,255,0)
blue = (0,0,255)
shape_turtle = turtle.Turtle()  # Create the Shape Turtle to be used for drawing shapes
shape_turtle.ht()               # Hide the Shape Turtle
shape_turtle.speed(0)           # Speed it up
shape_turtle.pu()               # Pull the pen up
the_turtle = turtle.Turtle()    # Create the Turtle object literally as the_turtle
the_turtle.speed(8)             # Speed it up.
the_turtle.pencolor(blue)       # Blue for the turtles path
shape_turtle.ht()               # No shape_turtle here.
#the_turtle.ht()                # Hide the Turtle for pixel perfect movement.
window = turtle.Screen()        # Create the screen object as window var
window.setworldcoordinates(0,SCRN_HEIGHT,SCRN_WIDTH,0)
                        # (lower_left_x_coord, lower_left_y_coord, upper_right_x_coord, upper_right_y_coord)
window.title("Turtle Maze Final v0.3 Manual")
maze = [[0]*SCRN_WIDTH for i in range(SCRN_HEIGHT)] # Maze list use [y][x] indexing
###DECLARE ALL GLOBAL VARIABLE INITILIZATIONS ABOVE THIS LINE ###

class Move: # Move Class for no real reason.
    '''
    Each Function Moves the_turtle used for event handeling
    '''
    def u():    # Go Up
        the_turtle.seth(270)                        # Face the_turtle North
        if maze[int(the_turtle.pos()[1])-1][int(the_turtle.pos()[0])] == 1:
                # .pos() returns a (x,y) tuple so you can index it and get the y, x coords
            print('collision detected')             # Collsion with barrier
        else:
            if maze[int(the_turtle.pos()[1])-1][int(the_turtle.pos()[0])] == 9:
                print('! You Reached The End !')    # Collision with end point
                window.bye()                        # Closes the turtle screen
            else:
                if int(the_turtle.pos()[1])-1 < 0:
                    print('edge of screen collision')   # Collision with the screen edges
                else:
                    the_turtle.fd(1)                    # If no collision detection then move forward
                    maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2 # and mark the path.
    def d():    # Go Down
        the_turtle.seth(90)
        if maze[int(the_turtle.pos()[1])+1][int(the_turtle.pos()[0])] == 1:
            print('collision detected')
        else:
            if maze[int(the_turtle.pos()[1])+1][int(the_turtle.pos()[0])] == 9:
                print('! You Reached The End !')
                window.bye()
            else:
                if int(the_turtle.pos()[1])+1 > SCRN_HEIGHT:
                    print('border collision')
                else:
                    the_turtle.fd(1)
                    maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
    def l():    # Go Left
        the_turtle.seth(180)
        if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])-1] == 1:
            print('collision detected')
        else:
            if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])-1] == 9:
                print('! You Reached The End !')
                window.bye()
            else:
                if int(the_turtle.pos()[0])-1 < 0:
                    print('border collision')
                else:
                    the_turtle.fd(1)
                    maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
    def r():    # Go Right
        the_turtle.seth(0)
        if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])+1] == 1:
            print('collision detected')
        else:
            if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])+1] == 9:
                print('! You Reached The End !')
                window.bye()
            else:
                if int(the_turtle.pos()[0])+1 > SCRN_WIDTH:
                    print('border collision')
                else:
                    the_turtle.fd(1)
                    maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
def in_boundary(x,y):
    '''
    Returns bool true if x,y are in bounds of screen
    '''
    if SCRN_WIDTH-1 >= x >= 0 and SCRN_HEIGHT-1 >= y >= 0:
        return True
    else:
        return False
def draw_shape(x, y):
    '''
    On mouse click takes the xy of mouse and draws a shape
    with the xy being the upper left of the object
    '''
    shape_turtle.ht()   # No shape_turtle here.
    x = int(x)          # No Floats Here.
    y = int(y)          # Next line takes User Input 
    shape_type = window.textinput('Shapes', 'Enter a shape type: square, triangle') 
    print('drawing shape at {},{}'.format(x,y)) # Print the coords in the console.
    if shape_type.lower() == 'square':          # If a square was chosen
        size = int(window.textinput('Square', 'Enter a number for the length of the squares sides in pixels'))
        shape_turtle.pu()           # Pen Up          NOTE: These are all calls to shape turtle
        shape_turtle.setpos(x, y)   # Move the shape_turtle to mouse x,y
        shape_turtle.pd()           # Pen Down
        shape_turtle.seth(0)        # Face East
        for step in range(size):    # For Pixel Length of Side.
            shape_turtle.fd(1)      # Mov forward 1 pixel and mark on map
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True: # Check if in Bounds.
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(90)       # Face South
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(180)      # Face West
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(270)      # Face North
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.pu()           # Put the pen back up
    elif shape_type.lower() == 'triangle':      # If triangle was chosen.
        size = int(window.textinput('Triangle', 'Enter a number for the length of the triangles sides in pixels'))
        shape_turtle.pu()
        shape_turtle.setpos(x, y)
        shape_turtle.pd()
        shape_turtle.seth(0)
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.right(120) # Triangles require angles.
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.right(120)
        for step in range(size):
            shape_turtle.fd(1)
            if in_boundary(int(shape_turtle.pos()[0]), int(shape_turtle.pos()[1])) == True:
                maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
    elif shape_type.lower() == 'circle':
        print('cant circle yet')# PI does wut.
    shape_turtle.ht()           # No shape turtle here.
    window.listen()             # Resume Event Handeling
def maze_dump():                # Used to confirm that the maze variable is working.
    start_time = time.time()    # Begin Timing.
    print('writing maze variable to maze_file.txt in this programs folder...')
    maze_file = open('maze_file.txt', 'w')  # Open or Create maze_file.txt in this programs folder.
    for row in maze:            # Go line by line, top to bottom: 0,0 to SCRN_WIDTH,SCRN_HEIGHT.
        maze_file.write(''.join(str(s) for s in row)) # Convert the int values to str for writing.
        maze_file.write('\n')   # New line for each row.
    maze_file.close()           # Close the File, very important.
    end_time = time.time()      # Get the End Timing.
    print('maze dump done in seconds: {}'.format(format(end_time-start_time, '.3f')))

    ### USER INPUT  : DECLARE ALL FUNCTIONS ABOVE THIS LINE ###
while True:         # Get valid user input for start position.
    start_pos = []  # start fresh.
    try:            # try until correct user input
        start_pos = [int(i) for i in # Convert each item in the final list into an int from str.
                     window.textinput('Start', 'Enter a starting position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                    # Present the bounds on where you can place the start position and take input as str
                         0,SCRN_WIDTH-1,0,SCRN_HEIGHT-1)).split(' ') ]# Split the input string into a list of characers discarding the blank spaces
    except:         # It failed so just keep trying.
        pass
    if len(start_pos) == 2 and in_boundary(start_pos[0], start_pos[1]):
        break       # This checks to enuser the user has given 2 numbers for the x,y coordinates and that they are witin the bounds of the screen.
                    # This ends the loop due to valid user input.
while True:         # This loop same as above loop but for end position
    end_pos = []
    try:
        end_pos = [int(i) for i in
                   window.textinput('End', 'Enter a destination position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                       0,SCRN_HEIGHT-1,0,SCRN_HEIGHT-1)).split(' ')]
    except:
        pass
    if len(end_pos) == 2 and in_boundary(end_pos[0], end_pos[1]):
        break
    
    ### EXECUTE USER INPUT ###
the_turtle.pu()                         # Pull pen up.
the_turtle.setpos(end_pos[0],end_pos[1])# Move the_turtle to users input of x,y end position.
maze[end_pos[1]][end_pos[0]] = 9        # Mark the end position x,y inside the maze variable as 9 for collision detection.
the_turtle.pd()                         # Push pen down.
the_turtle.dot(4,'red')                 # Mark the end position x,y pixels on the screen as a red colored dot.
the_turtle.pu()
the_turtle.setpos(start_pos[0],start_pos[1])# Move the_turtle to users input of x,y start_position.
maze[start_pos[1]][start_pos[0]] = 4        # Mark the start position x,y inside the maze variable as 4 for collision detection.
the_turtle.pd()
the_turtle.dot(4,'green')                   # Mark the start position x,y pixels on the screen as a green colored dot.

    ### BEGIN EVENT HANDELING ###
window.onkeypress(Move.u, 'Up')      # Binding for Up Arrow Key.
window.onkeypress(Move.d, 'Down')    # Binding for Down Arrow Key.
window.onkeypress(Move.l, 'Left')    # * Left Arrow Key.
window.onkeypress(Move.r, 'Right')   # * Right Arrow Key.
window.onkeypress(maze_dump, 'd')    # * d Keyboard Key.
window.onclick(draw_shape)      # When user clicks, the draw_shape function gets called and passed the mouse x,y
window.listen()                 # Begin Event Handeling
    ### END EVENT HANDELING     : MUST BE LAST SECTION OF PROGRAM ###
