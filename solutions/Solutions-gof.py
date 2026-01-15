import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def check_life(x,y):
    if x==1 and (y==2 or y==3):
        return 1
    elif x==0 and y==3:
        return 1
    else:
        return 0

class Gof:
    _my_colors = ['#E0E0E0', 'green']
    _cmap = LinearSegmentedColormap.from_list('', _my_colors, len(_my_colors))    
    def __init__(self,N=10,M=10,filename=''):
        if filename != '':
            self.field=np.genfromtxt(filename).transpose()
            self.N, self.M=self.field.shape
        else:
            self.field=np.zeros((N,M))
            self.N=N
            self.M=M
            self.field[5,5]=1
            self.field[5,4]=1
            self.field[5,3]=1
        self.new_field=np.zeros(self.field.shape)
        self.sum=np.zeros(self.field.shape)
        
        self._check_status=np.vectorize(check_life)
        

    def play(self,steps=10):
        for i in range(steps):
            self.evolve()
            plt.pause(0.5)
            plt.imshow(self.field,cmap=self._cmap)
        plt.show()
    
    #these 2 next functions can be used to time loop vs arrays as they don't print
    def play_test(self,steps=100):
        for i in range(steps):
            self.evolve()
            
    def play_test2(self,steps=100):
        for i in range(steps):
            self.evolve2()
     
    #"pythonic" way 
    def evolve(self):
        self.sum[1:-1,1:-1]=self.field[:-2,1:-1]+self.field[2:,1:-1]\
        +self.field[1:-1,:-2]+self.field[1:-1,2:]\
        +self.field[:-2,:-2]+self.field[2:,2:]\
        +self.field[2:,:-2]+self.field[:-2,2:]
        
        self.new_field=self._check_status(self.field,self.sum)
        self.new_field, self.field = self.field, self.new_field

    
    #simple loop example
    def evolve2(self):
        for i in range(1,self.N-1):
            for j in range(1,self.M-1):
                sum=self.field[i-1,j-1]+self.field[i-1,j]\
                +self.field[i-1,j+1]+self.field[i,j+1]\
                +self.field[i+1,j]+self.field[i+1,j-1]\
                +self.field[i+1,j+1]+self.field[i,j-1]
                self.new_field[i,j]=check_life(self.field[i,j],sum)
                
        self.new_field, self.field = self.field, self.new_field        
        


if __name__=="__main__":

    game=Gof(filename="../data/ships.txt")
    game.play(50)





