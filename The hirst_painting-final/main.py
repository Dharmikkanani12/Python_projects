import matplotlib.pyplot as plt
import random

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

# Parameters for grid
num_dots = 100
dots_per_row = 10
dot_size = 300
spacing = dot_size / 3

# Create a figure and set up axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, dots_per_row * spacing)
ax.set_ylim(0, dots_per_row * spacing)
ax.axis("off")

# Draw dots in a grid
for i in range(num_dots):
    x = (i % dots_per_row) * spacing
    y = (i // dots_per_row) * spacing
    color = random.choice(color_list)
    ax.add_patch(plt.Circle((x, y), radius=dot_size / 10, color=[c/255 for c in color]))

# Save the result as an image
plt.gca().invert_yaxis()  # Invert y-axis to match the original orientation
plt.savefig("dot_pattern.png", bbox_inches="tight", pad_inches=0.1)
plt.show()
