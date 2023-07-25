import turtle  # Allows us to use turtles
wn = turtle.Screen()  # Creates a playground for turtles
bg = input('What background color would you like? ')  # Input bg color.
# List of permitted bg colors: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
wn.bgcolor(bg)  # Set the window BG color
wn.title("Hello, Tess!")  # Set the window title

tess = turtle.Turtle()  # Create a turtle, assign to tess
tess.color("blue")  # Tell tess to change her color
tess.pensize(3)  # Tell tess to set her pen width

tess.forward(50)  # Tell tess to move forward by 50 units
tess.left(120)  # Tell tess to turn by 120 degrees
tess.forward(50)  # Tell tess to move forward by 50 units

wn.mainloop()  # Wait for user to close window
