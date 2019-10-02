from scipy import ndimage

import numpy as np
from scipy import ndimage


marble_block = np.load(file="data/marble_block_1.npy")

center =ndimage.measurements.center_of_mass(marble_block.astype('float32'))
print(center)

shapeV=marble_block.shape
base=marble_block[shapeV[-1]]
print(base)
print(type(base))
print(base.shape)