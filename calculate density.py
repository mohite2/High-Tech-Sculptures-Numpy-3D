import os
import numpy as np

g = os.walk("./data/marble")
shape = np.load(file='data/shape_1.npy')

for path,dir_list,file_list in g:
    for file_name in file_list:
        file=os.path.join(path, file_name)
        block = np.load(file)

        # shape.astype('float32')
        if shape.shape == block.shape:
            #print(block)
            # v= float('nan')
            # print(v)
            block[shape == 0] =np.nan ##cannot convert float NaN to intege
            #print(block)
        block=block.astype('float32')
        density=np.nanmean(block)
        print(density)

