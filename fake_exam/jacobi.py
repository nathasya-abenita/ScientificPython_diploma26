import numpy as np
import matplotlib.pyplot as plt

class Jacobi:
    def __init__(self, m, n):
        # Define grid size as m by n matrix
        self.m, self.n = m, n

        # Initialize NumPy array
        self.mat = np.zeros((m, n))

        # Set initial boundary
        max_val = 200
        self.mat[:, 0] = np.linspace(0, max_val, m)
        self.mat[m-1, :] = np.linspace(max_val, 0, n)

        # Set the initial condition of the inner elements as 0.5
        self.mat[1:-1, 1:-1] = 0.5

    def evolve(self):
        # Compute neighbors
        new_mat = self.mat[:-2, 1:-1]  \
                + self.mat[1:-1, :-2] + self.mat[1:-1, 2:] \
                + self.mat[2:, 1:-1]
        # Swap
        self.mat[1:-1, 1:-1] = new_mat * 0.25  

    def run(self, n, filename='last_iteration.png'):
        for n_iter in range (n):
            self.animate(n_iter)
            self.evolve()
        plt.savefig(filename)

    def animate(self, n_iter):
        plt.imshow(self.mat)
        plt.title(f'number of iteration = {n_iter}')
        plt.colorbar()
        plt.xlim(0, self.n-0.5)
        plt.ylim(0, self.m-0.5)
        plt.pause(0.05)
        plt.clf()

if __name__ == '__main__':
    # Define grid size as m by n matrix
    m, n = 50, 50

    # Call the class
    jac = Jacobi(m, n)

    # Run
    jac.run(200)

