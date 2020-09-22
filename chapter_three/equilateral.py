import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

colors = ["blue", "yellow", "purple"]
for c in colors:
    tess.color(c)
    tess.forward(80)
    tess.left(120)

wn.mainloop()