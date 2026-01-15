import numpy as np
from matplotlib import pyplot as plt
import time

class GoF:
  def __init__(self, filename):
    self.field=np.genfromtxt(filename).transpose()
    self.new_field=np.zeros_like(self.field)
    self.sum=np.zeros_like(self.field)
    self.N,self.M=self.field.shape
    self.check_life_v=np.vectorize(self.check_life)
    
  def print(self):
    plt.clf()
    plt.imshow(self.field, cmap='summer')
    
  def run(self):
    for _ in range(100):
      self.evolve_r()
      plt.pause(0.1)
      self.print()
    plt.show()   
    plt.savefig("result.png")
   
  def run_time(self):
    t1=time.time()
    for _ in range(1000):
      self.evolve()
    t2=time.time()
    print(t2-t1)
    
  def run_time_r(self):
    t1=time.time()
    for _ in range(1000):
      self.evolve_r()
    t2=time.time()
    print(t2-t1)
    
  def run_time_v(self):
    t1=time.time()
    for _ in range(1000):
      self.evolve_v()
    t2=time.time()
    print(t2-t1)  
    
    
   
  def check_life(self,value,nsum):
    if (value==1) and ((nsum==2) or (nsum==3)):
      return 1
    elif (value==0) and (nsum==3):
      return 1
    else: 
      return 0
   
   
  def evolve(self):
    #remember it's python, don't port to C directly cause of negative index
    for i in range(self.N):
      ii=(i+1)%self.N
      for j in range(self.M):
        jj=(j+1)%self.M
        sum=self.field[i,j-1]+self.field[i,jj]+self.field[i-1,j]+self.field[ii,j]+self.field[i-1,jj]+self.field[i-1,j-1]+self.field[ii,j-1]+self.field[ii,jj]
        self.new_field[i,j]=self.check_life(self.field[i,j],sum)
    self.field, self.new_field = self.new_field, self.field
    
    
  def evolve_v(self):
    self.sum[1:-1,1:-1]=self.field[0:-2,1:-1]+self.field[0:-2,0:-2]\
      +self.field[0:-2,2:]+self.field[2:,0:-2]+self.field[2:,1:-1]+self.field[2:,2:]+self.field[1:-1,0:-2]+self.field[1:-1,2:]
    self.new_field=self.check_life_v(self.field,self.sum)
    self.field, self.new_field = self.new_field, self.field

  def evolve_r(self):
    self.sum[:,:]=np.roll(self.field,1,axis=0)+np.roll(self.field,-1,axis=0)+\
      np.roll(self.field,1,axis=1)+np.roll(self.field,-1,axis=1)+\
        np.roll(np.roll(self.field,-1,axis=0),1,axis=1)+\
        np.roll(np.roll(self.field,-1,axis=0),-1,axis=1)+\
        np.roll(np.roll(self.field,1,axis=0),1,axis=1)+\
        np.roll(np.roll(self.field,1,axis=0),-1,axis=1)
    self.new_field=self.check_life_v(self.field,self.sum)
    self.field, self.new_field = self.new_field, self.field

if __name__=='__main__':
  game=GoF("../data/ships.txt")
  game.run_time()
  game.run_time_r()
  game.run_time_v()
