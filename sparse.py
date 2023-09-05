import numpy as np
from scipy.sparse import csr_matrix


class ADH:
    AA=([[0 for x in range(3)]for y in range(5)])
    def __init__(self, rows, columns):
        
        self.rows = rows
        self.columns = columns
        self.AA=np.array([[0 for x in range(self.columns)]for y in range(self.rows)])

    def Insert(self, row, column, value):
        self.AA[row][column] = value

    def Remove(self, row, column):
        u = self.arr[row][column]
        self.arr[row][column] = 0
        return u
        self.arr[row][column] = value

    def Get(self, row, column):
        return self.arr[row][column]

    def myfunc(self):
        print(self.arr[3][4])

    def Size(self):
        return (self.rows, self.columns)
    @staticmethod
    def Array2D_TO_Sparse(Array2D):
        S = csr_matrix(Array2D)
        return S
    @staticmethod
    def Sparse_TO_Array2D(sparse):
        A = sparse.todense()
        return A
    def __add__(self, o):
        C=np.array(self.AA)
        D=np.array(o.AA)
        F=C+D
        return F
    def __sub__(self, o):
        C=np.array(self.AA)
        D=np.array(o.AA)
        F=C-D
        return F
