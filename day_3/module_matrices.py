import numpy as np

class MyMatrix:
    def __init__ (self, n):
        self.n = n
        self.matrix = np.random.random((n, n)) # create n x n matrix

    def inverse(self):
        return np.linalg.inv(self.matrix)
    
    def determinant(self):
        return np.linalg.det(self.matrix)
    
    def eigenvalues(self):
        return np.linalg.eigvals(self.matrix)
    
    def __add__ (self, other):
        return self.matrix + other.matrix
    
    def __mul__ (self, other):
        return np.matmul(self.matrix, other.matrix)
    
if __name__ == '__main__':
    N=4
    matrix1=MyMatrix(N) #creates a square matrix
    matrix2=MyMatrix(N)
    print(matrix1.inverse())
    print(matrix1.determinant())
    print(matrix1.eigenvalues())
    print(matrix1+matrix2)
    print(matrix1*matrix2)