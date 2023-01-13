import unicornhathd
import numpy as np

# Initialize the Unicorn HAT HD
unicornhathd.set_layout(unicornhathd.PHAT)
unicornhathd.brightness(0.5)
width, height = unicornhathd.get_shape()

# Create an array to represent the up arrow
up_arrow = np.array([
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0]
])

# Rotate the array to make it display correctly on the Unicorn HAT HD
up_arrow = np.rot90(up_arrow)

# Place the arrow array on the center of the 16x16 matrix
zero_arr = np.zeros((16,16))
x_pos = int(16/2 - 6/2)
y_pos = int(16/2 - 8/2)
zero_arr[x_pos:x_pos+6, y_pos:y_pos+8] = up_arrow

# Set the pixels of the Unicorn HAT HD to match the array
for x in range(width):
    for y in range(height):
        pixel = zero_arr[x, y]
        unicornhathd.set_pixel(x, y, 255, 0, 0) if pixel == 1 else unicornhathd.set_pixel(x, y, 0, 0, 0)

# Show the arrow
unicornhathd.show()

