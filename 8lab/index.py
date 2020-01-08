import helper.helper as h
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy import integrate

def main():
    arrN=[10,20,40,80,160]
    a=0
    b=np.pi/2

    with open('output.dat', 'a') as output:
        print('\n---------------Metadata----------------', file=output)

        for k, v in h.Helper.getMeta('Kirill', 'Telegin', '3430302/80004').items():
            print(k, v, file=output)

        defListInterpolateFunction = []
        defListInterpolateFirstDer = []
        defListInterpolateSecondDer = []
        defListInterpolateThridDer = []
        defListIntegrate = []

        for N in arrN:
            x = np.arange(a, b, b/N)
            y = 1/(1+np.sin(x)) ** 2
            cs = CubicSpline(x, y)
            h = (b-a)/(4*N)
            xs = np.arange(0, 4*N*h, h)
            ys = 1/(1+np.sin(xs)) ** 2
            print('[a,b]:\n{}'.format(xs), file=output)
            print('current N: {}'.format(N), file=output)
            print('========================= function ==============================', file=output)
            print('S(x):\n {}'.format(cs(x)), file=output)
            print('Defect\n {}'.format(defectAprx(ys, cs(xs))), file=output)
            defListInterpolateFunction.append(defectAprx(ys, cs(xs)))
            print('===================== first derivative ==========================', file=output)
            print('S(x):\n {}'.format(cs(x,1)), file=output)
            print('Defect\n {}'.format(defectAprx(ys, cs(xs,1))), file=output)
            defListInterpolateFirstDer.append(defectAprx(ys, cs(xs,1)))
            print('==================== second derivative ==========================', file=output)
            print('S(x):\n {}'.format(cs(x,2)), file=output)
            print('Defect\n {}'.format(defectAprx(ys, cs(xs,2))), file=output)
            defListInterpolateSecondDer.append(defectAprx(ys, cs(xs,2)))
            print('===================== third derivative ==========================', file=output)
            print('S(x):\n {}'.format(cs(x,3)), file=output)
            print('Defect\n {}'.format(defectAprx(ys, cs(xs,3))), file=output)
            defListInterpolateThridDer.append(defectAprx(ys, cs(xs,3)))
            print('=========================== integral ============================', file=output)
            a = x[0]
            b = x[-1]
            integral = integrate.quad(lambda x: 1/(1+np.sin(x)) ** 2,a,b)
            print('integral {}'.format(integral[0]), file=output)
            print('defect integral {}'.format(integral[1]), file=output)
            defListIntegrate.append(integral[1])
            print('=================================================================', file=output)

            with open('output.dat', 'a') as output:
                print('Ratio of errors in spline function', file=output)
                for item in overTo(defListInterpolateFunction):
                    print(item, file=output)
                print('Ratio of errors in spline first derivative', file=output)
                for item in overTo(defListInterpolateFirstDer):
                    print(item, file=output)
                print('Ratio of errors in spline second derivative', file=output)
                for item in overTo(defListInterpolateSecondDer):
                    print(item, file=output)
                print('Ratio of errors in spline third derivative', file=output)
                for item in overTo(defListInterpolateThridDer):
                    print(item, file=output)
                print('Ratio of errors in integral', file=output)
                for item in overTo(defListIntegrate):
                    print(item, file=output)

            x = np.arange(a, b, b/40)
            y = 1/(1+np.sin(x)) ** 2
            fig, ax = plt.subplots(figsize=(6.5, 4))
            ax.plot(x, y, 'o', label='data')
            ax.plot(xs, cs(xs), label="spline")
            ax.plot(xs, cs(xs, 1), label="spline der1")
            ax.plot(xs, cs(xs, 2), label="spline der2")
            ax.plot(xs, cs(xs, 3), label="spline der3")
            ax.legend(loc='lower left', ncol=2)
            plt.savefig('graph.png')

def defectAprx(ys, cs):
    e = ys - cs
    return max(e)

def overTo(arr):
    bufArr = []
    bufArr.append(arr[1]/arr[0])
    bufArr.append(arr[2]/arr[1])
    bufArr.append(arr[3]/arr[2])
    bufArr.append(arr[4]/arr[3])
    return bufArr

main()
