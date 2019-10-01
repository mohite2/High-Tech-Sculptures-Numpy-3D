import os
import numpy as np

g = os.walk("./data")

for path,dir_list,file_list in g:
    for file_name in file_list:
        file=os.path.join(path, file_name)
        marble_block = np.load(file)
        print(marble_block.shape)


