import numpy as np
from PIL import Image

# Create 3D numpy array of zeros, then replace zeroes (black pixels) with yellow pixels
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a patch
data[0:2, 1:3] = [255, 200, 233]
data[3:6, 1:6] = [200, 221, 240]

img = Image.fromarray(data, "RGB")
img.save("canvas.png")

