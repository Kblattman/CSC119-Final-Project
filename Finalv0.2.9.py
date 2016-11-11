import turtle
import time

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
#the_turtle.ht()              # Hide the Turtle for pixel perfect movement.
window = turtle.Screen()     # Create the screen object as window var
window.setworldcoordinates(0,screen_height,screen_width,0)
# llx lly urx ury
window.title("Turtle Maze Final v0.2.5")

maze = [[0]*screen_width for i in range(screen_height)] # Maze list
# maze[y][x]

###DECLARE ALL GLOBAL VARIABLE INITILIZATIONS ABOVE THIS LINE ###
class Move:
    '''
    Each Function Moves the_turtle used for event handeling
    '''
    def u():
        the_turtle.seth(270)
        if maze[int(the_turtle.pos()[1])-1][int(the_turtle.pos()[0])] == 1:
            print('collision detected')
        else:
            if int(the_turtle.pos()[1])-1 < 0:
                print('border collision')
            else:
                the_turtle.fd(1)
                maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
    def d():
        the_turtle.seth(90)
        if maze[int(the_turtle.pos()[1])+1][int(the_turtle.pos()[0])] == 1:
            print('collision detected')
        else:
            if int(the_turtle.pos()[1])+1 > screen_height:
                print('border collision')
            else:
                the_turtle.fd(1)
                maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
    def l():
        the_turtle.seth(180)
        if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])-1] == 1:
            print('collision detected')
        else:
            if int(the_turtle.pos()[0])-1 < 0:
                print('border collision')
            else:
                the_turtle.fd(1)
                maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
    def r():
        the_turtle.seth(0)
        if maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])+1] == 1:
            print('collision detected')
        else:
            if int(the_turtle.pos()[0])+1 > screen_width:
                print('border collision')
            else:
                the_turtle.fd(1)
                maze[int(the_turtle.pos()[1])][int(the_turtle.pos()[0])] = 2
        
def draw_shape(x, y):
    '''
    On mouse click takes the xy of mouse and draws a shape
    with the xy being the upper left of the object
    '''
    x = int(x)
    y = int(y)
    shape_type = window.textinput('Shapes', 'Enter a shape type. EX: square, triangle, circle')
    print('draw shape at {},{}'.format(x,y))
    if shape_type.lower() == 'square':
        size = int(window.textinput('Square', 'Enter a number for the length of the squares sides in pixels'))
        shape_turtle.pu()
        shape_turtle.setpos(x, y)
        shape_turtle.pd()
        shape_turtle.seth(0)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(90)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(180)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.seth(270)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.pu()
    elif shape_type.lower() == 'triangle':
        size = int(window.textinput('Triangle', 'Enter a number for the length of the triangles sides in pixels'))
        shape_turtle.pu()
        shape_turtle.setpos(x, y)
        shape_turtle.pd()
        shape_turtle.seth(0)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.right(120)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        shape_turtle.right(120)
        for step in range(size):
            shape_turtle.fd(1)
            maze[int(shape_turtle.pos()[1])][int(shape_turtle.pos()[0])] = 1
        pass # Draw a triangle
    elif shape_type.lower() == 'circle':
        # Must be Redone to allow adding to the maze 2dList as it draws
        shape_turtle.pu()
        shape_turtle.setpos(x, y)
        shape_turtle.pd()
        shape_turtle.circle(20)
        shape_turtle.pu()
    window.listen()

def maze_dump():
    print('maze dump')
    maze_file = open('maze_file.txt', 'w')
    for row in maze:
        maze_file.write(''.join(str(s) for s in row))
        maze_file.write('\n')
    maze_file.close()
    print('maze dump done')

### DECLARE ALL FUNCTIONS ABOVE THIS LINE ###
                                                    # Empty Space
### USER INPUT ###
while True:
    start_pos = []
    try:
        # This is a very long line... but it works lol.
        start_pos = [int(i) for i in
                     window.textinput('Start', 'Enter a starting position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                         0,screen_width,0,screen_height)).split(' ') ]
    except:
        pass
    if len(start_pos) == 2:
        # Ensure player starting position input is within the screen boundary
        if screen_width >= start_pos[0] >= 0:
            if screen_height >= start_pos[1] >= 0:
                break
            else:
                pass
        else:
            pass

while True:
    end_pos = []
    try:
        # Another long line...
        end_pos = [int(i) for i in
                   window.textinput('End', 'Enter a destination position: x y\nX Between {} and {}\nY Between {} and {}'.format(
                       0,screen_height,0,screen_height)).split(' ')]
    except:
        pass
    if len(end_pos) == 2:
        # Ensure player end position input is within the screen boundary
        if screen_width >= end_pos[0] >= 0:
            if screen_height >= end_pos[1] >= 0:
                break
            else:
                pass
        else:
            pass

# Mark end pos
the_turtle.pu()
the_turtle.setpos(end_pos[0],end_pos[1])
maze[end_pos[0]][end_pos[1]] = 9
the_turtle.pd()
the_turtle.dot(4,'red')

# Put the_turtle at the user input position.
the_turtle.pu()
the_turtle.setpos(start_pos[0],start_pos[1])
maze[start_pos[0]][start_pos[1]] = 2
the_turtle.pd()
the_turtle.dot(4,'green')

### BEGIN EVENT HANDELING ###
window.onkey(Move.u, 'Up')
window.onkey(Move.d, 'Down')
window.onkey(Move.l, 'Left')
window.onkey(Move.r, 'Right')
window.onkey(maze_dump, 'd')
window.onclick(draw_shape)

window.listen()
### END EVENT HANDELING : MUST BE LAST SECTION OF PROGRAM ###
