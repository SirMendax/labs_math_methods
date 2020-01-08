import helper.helper as h
import numpy as np
from scipy.optimize import root

x=np.arange(-np.pi/2, np.pi/2)
def func(x):
    return np.tan(x) - x
arrSol = []
for item in x:
    arrSol.append(root(func, item).x)
print(x)
print(arrSol)
