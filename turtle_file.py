# import turtle
# from turtle import pensize
# wn = turtle.Screen()
# tess = turtle.Turtle()
# wn.title("Hello, Tess!")


# bg_color = input("Enter bgcolor!")
# wn.bgcolor(bg_color)
# color = input("Enter Tesses color!")
# tess.color(color)
# tess.shape("turtle")


# def user_choice():
#     pensize_choice = "WRONG"
#     while pensize_choice.isdigit() == False:
#         pensize_choice = input("Please enter the pen size")
#     return int(pensize_choice)

# tess.pensize(user_choice())

# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# wn.mainloop()


import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for i in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.mainloop()