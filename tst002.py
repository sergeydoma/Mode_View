import multiprocessing
from multiprocessing import set_start_method
from multiprocessing import Process

import numpy as np
from numpy import ones
from numpy import zeros


# task executed in a child process
def task():
    # declare the global variable
    global data
    # check some data in the array
    print('data Tack', data[:5, :3] )
    # change data in the array
    data.fill (0.0)
    # confirm the data was changed
    print ('global data', data[:5, :3])


# protect the entry point
if 1 == 1:
    print ( "Number of cpu : ", multiprocessing.cpu_count () )

    # ensure we are using fork start method
    set_start_method('fork')
    # define the size of the numpy array
    n = 10000
    # create the numpy array
    # data = ones ( (n, n) )
    data = np.array([
        [1, 9, 2],
        [1, 0, -1],
        [3, 5, 2],
        [3, 3, 2],
        [5, 8, 9],
    ])
    # create a child process
    child = Process(target=task)
    # start the child process
    child.start ()
    # wait for the child process to complete
    child.join ()
    # check some data in the array
    print ( 'data 2-2 =', data[:5, :3] )