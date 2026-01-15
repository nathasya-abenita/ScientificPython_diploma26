import time
from module_nonlinear_fit import NonlinearFit2D
import numpy as np

n_iter = 200
time_list = []

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

    for _ in range (n_iter):

        t = time.time()

        # Call the class
        fit = NonlinearFit2D(x_inp, y_inp, func, dfunc1, dfunc2)
        b1, b2 = fit.perform_fit(b1_init, b2_init, print_iteration=False)

        # Compute time
        time_list.append(time.time() - t)

    # Print output
    time_array = np.array(time_list)
    print(f'Testing program with {n_iter} simulations...')
    print(f'Running time average: {time_array.mean()} seconds')
    print(f'Running time std: {time_array.std()} seconds')