from collections import OrderedDict
import numpy as np

class Decision(object):
    def __init__(self, array, vector):
        self.array = array
        self.vector = vector

    def getAllValue(self):
        self.setSolution(self.array, self.vector)
        if(self.getSolution() == "singular matrix"):
            allValue = OrderedDict({
                "Solution for current parameter\n": "undefined",
                "The determinant of matrix\n": np.linalg.det(self.array)
            })
        else:
            self.setCondNum(self.array)
            self.setVecRes(self.array, self.vector, self.solution)
            allValue = OrderedDict({
                'Solution for current parameter\n': self.getSolution(),
                'Condition number for current solution\n': self.getCondNum(),
                'Inverse condition number for current solution\n': 1/self.getCondNum(),
                'Redisual vector for current solution\n': self.getVecRes(),
            })
        return allValue

    def setSolution(self, array, vector):
        """Calculation of the solution to a system of equations"""
        try:
            self.solution = np.linalg.solve(array, vector)
        except:
            self.solution = 'singular matrix'
            print('Error in solving the system of equations')


    def getSolution(self):
        """Return the solution of the system of equations"""
        return self.solution

    def setCondNum(self, array):
        """Calculation of the condition numbers to a system of equations"""
        try:
            self.condNum = np.linalg.cond(array)
        except:
            print('error in computed condition number')

    def getCondNum(self):
        """Return the condition numbers of the system of equations"""
        return self.condNum

    def setVecRes(self, array, vector, solution):
        """Calculation of the residual vector of the system of equations"""
        try:
            self.vecRes = np.array(vector) - np.dot(array, solution)
        except:
            print('error in computed redisual vector')

    def getVecRes(self):
        """Return the residual vector of the system of equations"""
        return self.vecRes

    def getDefect(A1, B1, A2, B2):
        """Calculation of the defect in solving the system of equations"""
        try:
            X1 = np.linalg.solve(A1, B1)
            X2 = np.linalg.solve(A2, B2)
            return X1 - X2
        except:
            return 'singular matrix'
