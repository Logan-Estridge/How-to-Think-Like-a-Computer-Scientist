
import turtle
wn = turtle.Screen()            # Set up the window and its attributes
wn.bgcolor('lightgreen')
wn.title('Tess and Alex')

tess = turtle.Turtle()          # Create Tess and set some attributes
tess.color('hotpink')
tess.pensize(5)

alex = turtle.Turtle()          # Create Alex

tess.forward(80)                # Tess draws an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)                 # Tess turns around and moves away from origin
tess.forward(80)

alex.forward(50)                # Alex draws a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
