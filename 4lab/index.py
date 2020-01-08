import numpy as np
import helper.helper as h
import lab as l

def main():
    floatA = np.transpose(np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float32))
    doubleA = np.transpose(np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float64))

    floatCSCA = h.Helper.getCscMatrix(floatA)
    doubleCSCA = h.Helper.getCscMatrix(doubleA)

    floatB = np.array(h.Helper.getVector('vector.dat'), dtype = np.float32)
    doubleB = np.array(h.Helper.getVector('vector.dat'), dtype = np.float64)

    floatP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float32)
    doubleP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float64)

    with open('output.dat', 'a') as output:
        print('\n============================Metadata============================', file=output)
        for k, v in h.Helper.getMeta('Kirill', 'Telegin', '3430302/80004').items():
            print(k, v, file=output)
        print("\nMatrix", file=output)
        print(floatCSCA, file=output)
        print("\nColumn vector", file=output)
        print(floatB, file=output)
        print('\n============================Single precision============================', file=output)
    printDesicion(floatCSCA, floatB, floatP)

    with open('output.dat', 'a') as output:
        print('\n============================Double precision============================', file=output)
    printDesicion(doubleCSCA, doubleB, doubleP)

    with open('output.dat', 'a') as output:
        print('\n============================Defect decision============================', file=output)
        bufFloatA = h.Helper.paramAddArray(floatP[0], floatCSCA, 0, 0)
        bufFloatB = h.Helper.paramAddArray(2*floatP[0], floatB, 0)
        bufDoubleA = h.Helper.paramAddArray(doubleP[0], doubleCSCA, 0, 0)
        bufDoubleB = h.Helper.paramAddArray(2*doubleP[0], doubleB, 0)
        print(l.Decision.getDefect(bufFloatA, bufFloatB, bufDoubleA, bufDoubleB), file=output)

def printDesicion(A, B, P):
    for i in range(len(P)):
        bufA = h.Helper.paramAddArray(P[i], A, 0, 0)
        bufB = h.Helper.paramAddArray(2*P[i], B, 0)
        with open('output.dat', 'a') as output:
            print('\nparameter value : {} \n'.format(P[i]), file=output)
            for k, v in l.Decision(bufA, bufB).getAllValue().items():
                print(k, v, file=output)

main()
