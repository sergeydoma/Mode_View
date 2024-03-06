# share numpy array via pipe
from multiprocessing import Process
from multiprocessing import Pipe

import numpy as np
from numpy import ones


# create a 2d numpy array
arr = np.array([[1, 2, 3, 4],
                [2, 0, 0, 2],
                [3, 1, 1, 0]])
# split the array into 2 subarrays horizontally
sub_arrays = np.hsplit(arr, 2)
# display the sub_arrays
print(sub_arrays)

print(sub_arrays.pop(0))