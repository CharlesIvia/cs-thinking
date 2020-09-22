import turtle
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.color("red")

for angle in angles:
    pirate.forward(100)
    pirate.left(angle)

wn.mainloop()
