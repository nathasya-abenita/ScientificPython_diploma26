import numpy as np
import matplotlib.pyplot as plt

class GameOfLife:

    def update_matrix (self, cell, neighbor):
        """ Update each cell status (LIVING, DEAD) """

        # Apply rules
        if cell: # Living cell case
            if (neighbor != 2) and (neighbor != 3):
                return 0
            else:
                return 1
        else: # Dead cell case
            if (neighbor == 3):
                return 1
            else:
                return 0
            
    def display(self, mat_list):
        for i in range (len(mat_list)):
            plt.imshow(mat_list[i])
            plt.title(f'Iteration number: {i}')
            plt.pause(0.1)
        plt.show()

    def generate_neighbor(self, mat, boundary_type):
        if boundary_type == 'kill':
            # Initialize boundary with zero neighbors to kill anything there
            neighbor = np.zeros(mat.shape)

            # Compute the neighbor
            neighbor[1:-1, 1:-1] = mat[0:-2, :-2] + mat[:-2, 1:-1] + mat[:-2, 2:] \
                                    + mat[1:-1, :-2] + mat[1:-1, 2:] \
                                    + mat[2:, :-2] + mat[2:, 1:-1] + mat[2:, 2:]
            
        elif boundary_type == 'periodic_pad':
            # Initialize boundary with zero neighbors to kill anything there
            mat_extended = np.pad(mat, 1, 'wrap')

            # Compute the neighbor
            neighbor = mat_extended[0:-2, :-2] + mat_extended[:-2, 1:-1] + mat_extended[:-2, 2:] \
                    + mat_extended[1:-1, :-2] + mat_extended[1:-1, 2:] \
                    + mat_extended[2:, :-2] + mat_extended[2:, 1:-1] + mat_extended[2:, 2:]
            
        elif boundary_type == 'periodic_roll':
            neighbor = (
                        np.roll(np.roll(mat, -1, axis=0), -1, axis=1) +     # up-left
                        np.roll(mat, -1, axis=0) +                          # up
                        np.roll(np.roll(mat, -1, axis=0),  1, axis=1) +     # up-right
                        np.roll(mat, -1, axis=1) +                          # left
                        np.roll(mat,  1, axis=1) +                          # right
                        np.roll(np.roll(mat,  1, axis=0), -1, axis=1) +     # down-left
                        np.roll(mat,  1, axis=0) +                          # down
                        np.roll(np.roll(mat,  1, axis=0),  1, axis=1)       # down-right
                        )
    
        else:
            raise ValueError ('Choose correct boundary type!')
        return neighbor

    def run(self, file_name, boundary_type):
        """ Run Game of Life simulation and plot it """

        # Read initial condition
        mat = np.genfromtxt(file_name).transpose()

        # Define number of iterations
        n_iter = 1000

        # Initialize matrix of each iteration
        mat_list = [mat]
    
        # Vectorize the function
        vec_update_matrix = np.vectorize(self.update_matrix)

        # Perform iteration
        for i in range (n_iter):

            # Count neighbor
            neighbor = self.generate_neighbor(mat, boundary_type)

            # Update matrix
            mat = vec_update_matrix(mat, neighbor)

            # Save new matrix to the new list
            mat_list.append(mat)
                
        # Show animation
        self.display(mat_list)

if __name__ == '__main__':
    gof = GameOfLife()
    gof.run(file_name="./data/ships.txt", boundary_type='periodic_roll') # boundary_type = ['kill', 'periodic_roll', 'periodic_pad']
