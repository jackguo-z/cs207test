import numpy as np

def L2(v, *args):
    """
    Returns the L2 norm of a vector.
     
    INPUTS
    =======
    v: a vector of floats, required
       The vector you want to compute L2 norm on
    *args: a vector of floats of the same dimension as v, optional
       If specified, they will be timed with elements of v to calculate the weighted L2 norm
       
    RETURNS
    =======
    L2 norm: a float
       The L2 norm of input vector v. Weighted if *args is given
       ValueError will be raised when input weights and v do not have the same length
       
    EXAMPLES
    =======
    >>> L2([3,4])
    5.0
    
    >>> L2([3,4],[1,2])
    8.5440037453175304
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)
