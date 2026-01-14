import numpy as np
import matplotlib.pyplot as plt

class GameOfLife:
    # Define neighbor indices (8 neighbors)
    neigh_idxs = [[1, -1], [1, 0], [1, 1], 
                [0, -1], [0, 1], 
                [-1, -1],[-1, 0], [-1, 1] ]
    
    def compute_neighbors (self, mat, boundary_type):
        """ Compute neighbors on each cell by applying periodic boundary """
        
        # Initialize neighbor matrix
        neighbor = np.zeros(mat.shape)

        # Iterate over each cell
        for i in range (len(mat)):
            for j in range (len(mat[0])):
                # Iterate over each adjacent neighbor
                for ni, nj in self.neigh_idxs:

                    # Boundary case
                    if (i == 0) or (j == 0) or (i == (len(mat) - 1)) or (j == (len(mat[0]) - 1)): 
                        if boundary_type == 'kill':
                            neighbor[i, j] = 0
                            break
                        elif boundary_type == 'periodic':
                            if mat[(i+ni) % len(mat), (j+nj) % len(mat[0])] == 1:
                                neighbor[i, j] += 1
                        else:
                            raise ValueError ('Choose correct boundary type!')
                        
                    # Interior case
                    else: # Compute neighbors
                        if mat[i+ni, j+nj] == 1:
                            neighbor[i, j] += 1
        return neighbor

    def update_matrix (sefl, mat, neighbor):
        """ Update each cell status (LIVING, DEAD) """

        # Iterate over each cell
        for i in range (len(mat)):
            for j in range (len(mat[0])):

                # Check number of neighbor
                n = neighbor[i, j]

                # Apply rules
                if mat[i, j]: # Living cell case
                    if (n != 2) and (n != 3):
                        mat[i, j] = 0
                else: # Dead cell case
                    if (n == 3):
                        mat[i, j] = 1
        return mat

    def run(self, file_name, boundary_type):
        """ Run Game of Life simulation and plot it """

        # Read initial condition
        mat = np.genfromtxt(file_name).transpose()

        # Define number of iterations
        n = 1000

        # Plot initial condition
        plt.imshow(mat)
        plt.xticks([]); plt.yticks([])
        plt.title('Iteration number: 0')
        plt.pause(0.25)

        # Perform iteration
        for i in range (n):
            # Count neighbor
            neighbor = self.compute_neighbors(mat, boundary_type)

            # Update matrix
            mat = self.update_matrix(mat, neighbor)
        
            # Plot
            plt.imshow(mat)
            plt.title(f'Iteration number: {i}')
            plt.pause(0.25)
        
        # Show animation
        plt.show()

if __name__ == '__main__':
    gof = GameOfLife()
    gof.run(file_name="./data/gun.txt", boundary_type='kill') # boundary_type = ['kill', 'periodic']
