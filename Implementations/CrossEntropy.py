import numpy as np 

def cross_entropy(y, y_):
    x = y_*np.log(y) + (1-y_)*np.log(1-y)
    cross_entropy = np.sum(x)
    return(cross_entropy)