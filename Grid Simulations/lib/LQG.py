import scipy as scp
from scipy import fftpack
import numpy as np

def TorusGFF(s=1000):
    x = np.linspace(0,1-1./s, s) #get s uniformly spaced numbers, they are the k/n
    energy = 4*np.sin(np.pi*x)**2
    energy = energy[None,:]+energy[:,None] #make it 2d by saying E(k1,k2) = E(k1)+E(k2)
    energy[0,0]=1E10 # We have to kill the constant case
    amplitude = 1./(energy)**.5 #the variance of the gaussian is the inverse of the energy
    modes =   np.random.normal(size=(s,s))*amplitude +  \
           1j*np.random.normal(size=(s,s))*amplitude #Randomize the real and complex modes
    return np.real(fftpack.fft2(modes)/s) #the division by s is due to the normalisation in fft2

# This is a terrible heuristic iterative solver to find the distances on a grid.
# it is a terrible idea, but it was fast to implement and sort of works
# It uses the fact that d(0,x) is the biggest 1-liptschitz function such that f(0)=0, and iteratively 
#tries to improve the functionx
def iterative_grid_solver(grid,max_iters = 400,dist = None,verbose = True): #should implement Dikjstra's instead?
    s = grid.shape[0] #size
    if dist is None:
        dist = 1E10+np.zeros_like(grid)
        dist[s//2,s//2] = 0
    for i in range(max_iters):
        if verbose and i%25 == 1: #give a result once every 25 iterations, skip the uninformative first one
            print(np.mean(dist))
        for l in range(s):
            for d in [-1,1]:
                p = s//2+l*d;
                dist[:,p%s] = np.amin([dist[:,(p-1)%s]+grid[:,p%s],
                                       dist[:,(p+1)%s]+grid[:,p%s],
                                       dist[:, p%s]],axis = 0)
                dist[p%s,:] = np.amin([dist[(p-1)%s,:]+grid[p%s,:],
                                       dist[(p+1)%s,:]+grid[p%s,:],
                                       dist[ p%s,:]],axis = 0)
    return dist