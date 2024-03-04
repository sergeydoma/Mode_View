# share numpy array via pipe
from multiprocessing import Process
from multiprocessing import Pipe

import numpy as np
from numpy import ones


# task executed in a child process
def task(pipe):
    # define the size of the numpy array
    # n = 10000
    # create the numpy array
    # data = ones ((n, n))
    data = np.array ( [
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9],
        ] )
    # check some data in the array
    print ('Data task ', data[:5, :3] )
    # send the array via a pipe
    pipe.send(data)


# protect the entry point
if 1 == 1:
    # create the shared pipe
    conn1, conn2 = Pipe ()
    # create a child process
    child = Process(target=task, args=(conn2,))
    # start the child process
    child.start ()
    # read the data from the pipe
    data = conn1.recv()
    # check some data in the array
    print ( "data out ",data[:5, :3] )