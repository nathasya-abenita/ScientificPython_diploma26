# Exercise 8
# Create a "wrapper class" for around numpy array for operations on matrices. You should be able to execute the following code:
# N=4
# matrix1=MyMatrix(N) #creates a square matrix
# matrix2=MyMatrix(N)
# print(matrix1.inverse())
# print(matrix1.determinant())
# print(matrix1.eigenvalues())
# print(matrix1+matrix2)
# print(matrix1*matrix2)

import numpy as np

class MyMatrix:
    def __init__(self, N):
        self.matrix = np.random.rand(N, N)
        self.dim=N

    def inverse(self):
        return np.linalg.inv(self.matrix)

    def determinant(self):
        return np.linalg.det(self.matrix)

    def eigenvalues(self):
        return np.linalg.eig(self.matrix)

    def __add__(self, other):
        result = MyMatrix(self.dim)
        result.matrix=self.matrix + other.matrix
        return result

    def __mul__(self, other):
        result = MyMatrix(self.dim)
        result.matrix=np.matmul(self.matrix, other.matrix)
        return result
      
    def __str__(self):
        return str(self.matrix)  
    
if __name__ == "__main__":
    N = 4
    matrix1 = MyMatrix(N)
    matrix2 = MyMatrix(N)
    print(matrix1.inverse())
    print(matrix1.determinant())
    print(matrix1.eigenvalues())
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)
  
    
