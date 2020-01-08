import helper.helper as h
import lab as l
import numpy as np

def main():
    floatA = np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float32)
    floatB = np.array(h.Helper.getVector('vector.dat'), dtype = np.float32)

    doubleA = np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float64)
    doubleB = np.array(h.Helper.getVector('vector.dat'), dtype = np.float64)

    floatP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float32)
    doubleP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float64)

    with open('output.dat', 'a') as output:
        print('\n============================Metadata============================', file=output)
        for k, v in h.Helper.getMeta('Kirill', 'Telegin', '3430302/80004').items():
            print(k, v, file=output)
        print("\nMatrix", file=output)
        print(floatA, file=output)
        print("\nColumn vector", file=output)
        print(floatB, file=output)
        print('\n============================Single precision============================', file=output)
    printDesicion(floatA, floatB, floatP)

    with open('output.dat', 'a') as output:
        print('\n============================Double precision============================', file=output)
    printDesicion(doubleA, doubleB, doubleP)


def printDesicion(A, B, P):
    for i in range(len(P)):
        bufA = h.Helper.paramAddArray(P[i], A, 0, 0)
        bufB = h.Helper.paramAddArray(0*P[i], B, 0)
        with open('output.dat', 'a') as output:
            print('\n----------------------------------------------------------------', file=output)
            print('parameter value : {}'.format(P[i]), file=output)
            print('----------------------------------------------------------------', file=output)
            for k, v in l.Decision(bufA, bufB).getAllValue().items():
                print(k, v, file=output)

main()
