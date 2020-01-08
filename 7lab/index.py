import helper.helper as h
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def main():
    arrN=[10,20,40,80,160]
    a=0
    b=np.pi/2

    with open('output.dat', 'a') as output:
        print('\n---------------Metadata----------------', file=output)
        for k, v in h.Helper.getMeta('Kirill', 'Telegin', '3430302/80004').items():
            print(k, v, file=output)
        for N in arrN:
            x = np.arange(a, b, b/N)
            y = 1/(1+np.sin(x)) ** 2
            cs = CubicSpline(x, y)
            h = (b-a)/(4*N)
            xs = np.arange(0, 4*N*h, h)
            ys = 1/(1+np.sin(xs)) ** 2
            print('[a,b]:\n{}'.format(xs), file=output)
            print('current N: {}'.format(N), file=output)
            print('S(x):\n {}'.format(cs(x)), file=output)
            print('Defect\n {}'.format(defectAprx(ys,cs(xs))), file=output)
            print('=================================================================', file=output)

    x = np.arange(a, b, b/40)
    y = 1/(1+np.sin(x)) ** 2
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(x, y, 'o', label='data')
    ax.plot(xs, cs(xs), label="spline")
    ax.legend(loc='lower left', ncol=2)
    plt.savefig('graph.png')


def defectAprx(ys, cs):
    e = ys - cs
    return max(e)

main()
