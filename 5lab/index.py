import numpy as np
import helper.helper as h
from scipy import linalg
from collections import OrderedDict

def main():
    fA = np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float32)
    dA = np.array(h.Helper.getMatrix('matrix.dat'), dtype = np.float64)
    fP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float32)
    dP = np.array([1.0000000, 0.0156250, 0.0000000], dtype = np.float64)
    fEps = np.finfo(np.float32).eps
    dEps = np.finfo(np.float64).eps

    with open('output.dat', 'a') as output:
        print('\n--------------------Metadata---------------------', file=output)
        for k, v in h.Helper.getMeta('Kirill', 'Telegin', '3430302/80004').items():
            print(k, v, file=output)
        print("\nMatrix", file=output)
        print(fA, file=output)
        print('\n----------------Single precision------------------', file=output)
        for i in range(len(fP)):
            print("====================================================", file=output)
            for k, v in getDesicion(fA,fP[i],fEps).items():
                print(k, v, file=output)
            print("====================================================", file=output)

    with open('output.dat', 'a') as output:
        print('\n-----------Double precision------------', file=output)
        for i in range(len(dP)):
            print("====================================================", file=output)
            for k, v in getDesicion(dA,dP[i],dEps).items():
                print(k, v, file=output)
            print("====================================================", file=output)


def ortVector(array):
    with open('output.dat', 'a') as output:
        print("\nОртогональность", file=output)
        bufOrtVect = np.zeros(shape=(len(array),len(array)))
        for i in range(len(array)):
            for j in range(len(array)):
                if(i == j):
                    continue
                else:
                    bufOrtVect[i][j] = np.dot(array[i], array[j])
        print(bufOrtVect, file=output)

def indexPerfomance(A, eigVect, eigValue, eps):
    bufIP = np.zeros(shape=(len(eigValue)))
    for i in range(len(eigValue)):
        bufIP[i] = np.linalg.norm(np.dot(A,eigVect[i]) - eigValue[i]*eigVect[i])/(len(eigVect)*eps*np.linalg.norm(A)*np.linalg.norm(eigVect))
    return max(bufIP)

def vectN(A,B):
    bufR = np.zeros(shape=(len(B[1]),len(B[1])))
    i = -1
    for row in B[1]:
        i += 1
        bufR[i] = np.dot(B[0],row) - np.dot(A,row)
    return bufR

def getDesicion(A, P, eps):
    A = h.Helper.paramAddArray(P, A, 0, 0)
    B = np.linalg.eig(A)
    allValue = OrderedDict({
        'Current parameter value\n': P,
        'Index perfomance\n': indexPerfomance(A,B[1],B[0], eps),
        'Eigenvalues\n': B[0],
        'Eigenvectors\n': B[1],
        'Redisual vectors\n': vectN(A,B),
    })
    return allValue

main()
