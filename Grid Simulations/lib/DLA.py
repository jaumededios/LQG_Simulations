from rtree import index
import numpy as np

def random_walk_from_infinity(idx, positions, ball_radius = 1, max_dist=1E3):
    epsilon = 0.05
    pos = max_dist*random_unit_vector() #start at a random place
    distance = 4*ball_radius #just initialize the distance to the nearest neigh to a lower bound
    
    while distance > 2*ball_radius:
        #update position with allowed jump
        pos += random_unit_vector()*(distance-(2-epsilon)*ball_radius) #move knowing that you won't hit
        #print pos
        #if we drift too far, force come back 
        #(should add a poisson kernel bias, but if we are too far away shouldn't change much)
        dist_from_orig = np.sum(pos**2)**.5 
        if dist_from_orig > 10*max_dist:
            pos = max_dist*random_unit_vector()
            
        # decide how much we should jump next time
        closest_object_id = idx.nearest(tuple(pos)*2, 1).next() # this be the closest object id
        closest_object = positions[closest_object_id] #check the closest object position
        distance = np.sum((pos-closest_object)**2)**.5 #compute the distance to it

    return pos