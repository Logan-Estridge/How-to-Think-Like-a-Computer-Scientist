# Creating turtle environment
import turtle
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Alex')

# Creating Alex
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.speed(0)

# Moving Alex
alex.penup()
size = 25
for i in range(10):
    size += 5
    alex.stamp()
    alex.forward(size)
alex.color("white")
alex.left(90)
alex.pendown()
alex.forward(100)

wn.mainloop()
