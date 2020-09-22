import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

colors = ["blue", "yellow", "purple", "red", "black", "blue"]
for c in colors:
    tess.color(c)
    tess.forward(100)
    tess.left(60)

wn.mainloop()
