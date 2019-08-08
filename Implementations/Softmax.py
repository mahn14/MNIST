# Dependencies
import numpy as np 


# Softmax Equation
def softmax(y):
    y = np.array(y)

    # stabilizing constant
    C = -max(y)

    # softmax calculations
    exps = C*np.exp(y + C) 
    sums = np.sum(exps)
    softmax_result = exps/sums

    return(softmax_result)

def softmax_derivative(p):
    
    if i == j:
        d = p[i]*(1-p[j])
    elif i != j:
        d = -p[i]*p[j]
    else:
        return("Warning: Index Problem")

    return(d)
