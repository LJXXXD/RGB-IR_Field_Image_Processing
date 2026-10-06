
import numpy as np


xs = np.array([(5, 8), (3, 6), (0, 14), (6,2)])
ys = []
print(xs)

for x in xs:
    print(x)
    y = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    ys.append(1/y)
    print(1/y)

yssum = np.sum(ys)
ys = np.asarray(ys)
ysnorm = ys/yssum
print("fitness", ys)
print("fitness norm", ysnorm)

rw = []

for i in range(4):
    rw.append(np.sum(ysnorm[0:i+1]))
print("Roulette Wheel", rw)