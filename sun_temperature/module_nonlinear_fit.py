import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

class NonlinearFit2D:
    """Fitting a scalar function with two fit parameters F(x; b1, b2)"""

    def __init__(
            self,
            x: np.ndarray,
            y: np.ndarray,
            func: Callable[[float, float, float], float],
            dfunc1: Callable[[float, float, float], float],
            dfunc2: Callable[[float, float, float], float]
    ):
        """
        x, y               : One-dimensional array with the same size, containing the data
        func(x, b1, b2)    : Function with two parameters
        dfunc1(x, b1, b2)  : First partial derivative of the function to the first fit parameter
        dfunc2(x, b1, b2)  : First partial derivative of the function to the second fit parameter
        """

        self.x          = x
        self.y          = y
        self.func_v     = np.vectorize(func)
        self.dfunc1_v   = np.vectorize(dfunc1)
        self.dfunc2_v   = np.vectorize(dfunc2)
        self.data_size  = len(x)

        self.b1_list    = []
        self.b2_list    = []
        pass

    def compute_descent_direction (self, jac, r):
        inv = np.linalg.inv(np.matmul(jac.transpose(), jac))
        return np.matmul(np.matmul(inv, jac.transpose()), r)
    
    def compute_std (self, b1, b2, jac):

        # Compute variance of error
        var = np.sum((self.y - self.func_v(self.x, b1, b2)) ** 2)
        var = var / (self.data_size - 2)

        # Compute standard errors
        se = var * np.linalg.inv(np.matmul(jac.transpose(), jac))

        # Compute standard deviation
        se1, se2 = np.sqrt(se[0, 0]), np.sqrt(se[1, 1])
        return se1, se2

    def update_fit(self, b1, b2, step_fit):

        # Construct residuals vector
        r = self.y - self.func_v(self.x, b1, b2)

        # Construct Jacobian matrix
        jac = np.zeros((self.data_size, 2))
        jac[:, 0] = self.dfunc1_v(self.x, b1, b2)
        jac[:, 1] = self.dfunc2_v(self.x, b1, b2)

        # Find descent direction
        delta_b = self.compute_descent_direction(jac, r)
        descent_magnitude = np.sum(delta_b ** 2)

        # Update fit parameters
        b1 += delta_b[0] * step_fit
        b2 += delta_b[1] * step_fit

        # Compute standard deviation
        se1, se2 = self.compute_std (b1, b2, jac)

        return b1, b2, se1, se2, descent_magnitude
    
    def perform_fit (self, b1, b2, step_fit=0.1, error_thr=1e-6, max_num_iter=1_000, print_iteration=False):

        # Set looping conditions
        num_iter = 0
        descent_magnitude = 999

        # Iterate until looping condition is reached
        while (descent_magnitude > error_thr) and (num_iter <= max_num_iter):
            # Update fit
            b1, b2, se1, se2, descent_magnitude = self.update_fit(b1, b2, step_fit)

            # Print iteration if asked
            if print_iteration:
                print(b1, b2, se1, se2, descent_magnitude)

            # Update number of iteration
            num_iter += 1

            # Save new parameters
            self.b1_list.append(b1)
            self.b2_list.append(b2)
            
        return b1, b2
    
    def plot_fit_iteration(self):
        # Create a color array based on row index or another column
        colors = np.arange(len(self.b1_list))  # or df['some_column'] for custom coloring

        # Fit parameters update
        fig, ax = plt.subplots(figsize=(9, 9))
        sc = ax.scatter(self.b1_list, self.b2_list, c=colors, cmap='viridis')  # Try 'plasma', 'coolwarm', etc.
        cb = fig.colorbar(sc, ax=ax, label='Iteration number', shrink=0.6)
        cb.set_ticks([colors.min(), colors.max()])  # only min and max ticks
        ax.set_xlabel(r'$\beta_1$')
        ax.set_ylabel(r'$\beta_2$')
        ax.set_title('Fit parameters values \nover the fitting process')
        ax.grid()

        plt.show()

if __name__ == '__main__':
    # Create functions to be fit
    func    = lambda x, b1, b2 : b1 / (x**5 * (np.exp(b2/x) - 1))
    dfunc1  = lambda x, b1, b2 : 1 / (x**5 * (np.exp(b2/x) - 1))
    dfunc2  = lambda x, b1, b2 : -1 * (b1 * np.exp(b2/x)) / (x**6 * (np.exp(b2/x) - 1)**2)

    # Read data for inputs
    file_name = './sun_temperature/sun_data.txt'
    data = np.genfromtxt(file_name)
    x_inp, y_inp = data[:, 0], data[:, 1]

    # Set initial fit parameters
    b1_init, b2_init = 1.0, 1.0

    # Call the class
    fit = NonlinearFit2D(x_inp, y_inp, func, dfunc1, dfunc2)

    # Perform fitting
    b1, b2 = fit.perform_fit(b1_init, b2_init, print_iteration=False)

    # Compute the temperature of the sun
    print('The temperature of the sun (in K) is', (14387.77) / b2)

    # Make fit parameter plot
    fit.plot_fit_iteration()