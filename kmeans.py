import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class KMeans:
    def __init__ (self, n_cluster, x, y, centroid_coords=[]):

        # Save data and number of clusters
        self.n_cluster = n_cluster
        self.x = x
        self.y = y
        self.x_min, self.x_max = x.min(), x.max()
        self.y_min, self.y_max = y.min(), y.max()
        self.delta_x = self.x_max - self.x_min
        self.delta_y = self.y_max - self.y_min


        # Decide initial guesses
        if (len(centroid_coords) == 0): # Automatic case
            self.centroid_coords = np.zeros((n_cluster, 2))
            self.centroid_coords[:, 0] = np.linspace(x.min(), x.max(), n_cluster)
            self.centroid_coords[:, 1] = np.linspace(y.min(), y.max(), n_cluster)
        else: # Manual case
            if (len(centroid_coords) == n_cluster):
                self.centroid_coords = np.array(centroid_coords)
            else:
                raise ValueError ('Number of initial guesses are not the same as chosen number of cluster!')
        
        # Decide initial cluster
        self.cluster_idxs = np.array([self.decide_cluster(x, y) for x,y in zip(x, y)])

        # Decide colors
        cmap = mpl.colormaps['viridis']
        self.colors = cmap(np.linspace(0, 1, n_cluster))

    def decide_cluster(self, x, y):
        distance = (self.centroid_coords[:, 0] - x) ** 2 + (self.centroid_coords[:, 1] - y) ** 2
        return distance.argmin()

    def update_centroids(self):
        for code in range (self.n_cluster):
            
            x_cluster = self.x[ self.cluster_idxs == code]
            y_cluster = self.y[ self.cluster_idxs == code]
            self.centroid_coords[code, :] = x_cluster.mean(), y_cluster.mean()
    
    def animate_iteration(self, num_iteration):
        # Plot for each cluster
        for code in range (self.n_cluster):
            x_cluster = self.x[ self.cluster_idxs == code]
            y_cluster = self.y[ self.cluster_idxs == code]
            plt.scatter(x_cluster, y_cluster, color=self.colors[code])
            plt.scatter(self.centroid_coords[:, 0], self.centroid_coords[:, 1], marker='*', color='red')
            plt.title(f'number of iteration: {num_iteration}')
            plt.xlim(self.x_min - self.delta_x * 0.1, self.x_max + self.delta_x * 0.1)
            plt.ylim(self.y_min - self.delta_y * 0.1, self.y_max + self.delta_y * 0.1)
        
        # Pause for animation and clear figure for next iteration
        plt.pause(0.1)
        plt.clf()
            
    def perform_cluster(self, plot_iteration=True):
        n_iteration = 50

        for n in range (n_iteration):
            print(self.centroid_coords)

            if plot_iteration:
                self.animate_iteration(n)

            # Update centroid
            self.update_centroids()
            
            # Update cluster indexes
            self.cluster_idxs = np.array([self.decide_cluster(x, y) for x,y in zip(x, y)])

        if plot_iteration:
            plt.show()
        pass
    
    def plot_data(self):
        plt.scatter(self.x, self.y)
        plt.xlabel('$x$'); plt.ylabel('$y$')
        plt.grid()
        plt.show()
    
if __name__ == '__main__':
    # Read data 
    filename = r'./data/s3.txt'
    data = np.genfromtxt(filename)
    x, y = data[:, 0], data[:, 1]

    # Call class
    cluster = KMeans(n_cluster=3, x=x, y=y, centroid_coords=[])

    # Plot data
    # cluster.plot_data()

    # Perform K-means clustering
    cluster.perform_cluster()

