# import numpy as np
#
# x = np.array([5, 2, 3, 1, 4, 5])
# y = np.array([0, 1, 0, 1, 0, 1])
#
#
# ans=np.logical_and(x != 0, y == 0)
#
# print(ans)
# print(y)
import math

import numpy as np
a = np.random.randint(0, 5, size=(5, 4))
print(a)
# b = a < 3
# print(b)
# c = b.astype(int)
# print(c)
d= (a < 3).astype(int)
print(d)
nan = float('nan')
a[d==0] =nan
print(a)