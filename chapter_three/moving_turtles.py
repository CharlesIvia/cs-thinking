import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("yellow")

tess.penup()
size = 20
for i in range(29):
    tess.stamp()  # Leave an impression on the canvas
    size = size + 3  # Increase the size of every iteration
    tess.forward(size)
    tess.right(24)

tess.color("purple")

wn.mainloop()