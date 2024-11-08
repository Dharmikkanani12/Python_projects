import random
from svg_turtle import SvgTurtle

# Set up the turtle to draw on an SVG canvas
t = SvgTurtle(800, 800)
t.speed("fastest")
t.penup()
t.hideturtle()

# Define color list
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), 
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), 
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), 
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), 
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), 
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

# Initial position setup
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

# Draw dots in a grid
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

# Save the result as an SVG file
with open("output.svg", "w") as file:
    file.write(t.save_as_svg())
