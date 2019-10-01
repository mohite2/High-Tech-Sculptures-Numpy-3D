#import os
import numpy as np
import scipy
from scipy import ndimage


marble_block = np.load(file="/data/marble_block_1.npy")
print(marble_block.shape)
image =ndimage.measurements.center_of_mass(marble_block.astype('float32'))
print(image)
#z=np.multiply.reduce(np.arange(21)+1)
#print(z,image)