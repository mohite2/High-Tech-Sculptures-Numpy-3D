import numpy as np
x=np.arange(24).reshape(4,3,2)
print(x)
base=x[3]
base=x[-1]
print(base)
corner1=base[0]
corner2=base[-1]
print(corner1,corner2)
print(corner1[0])
print(corner1[-1])
# corner3=base[]
# corner4=base[]
#
x=np.arange(24).reshape(4,2,3)
print(x)
base=x[-1]
print(base)
corner1=base[0]
corner2=base[-1]
print(corner1,corner2)
print(corner1[0])
print(corner1[-1])

x=np.arange(60).reshape(4,3,5)
print(x)
base=x[-1]
print(base)
corner1=base[0]
corner2=base[-1]
print(corner1,corner2)
print(corner1[0])
print(corner1[-1])
print(corner2[0])
print(corner2[-1])
