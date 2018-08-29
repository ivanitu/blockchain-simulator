'''
An approximation of network latency in the Bitcoin network based on the
following paper: https://ieeexplore.ieee.org/document/6688704/.

From the green line in Fig 1, we can approximate the function as:

    Network latency (sec) = 19/300 sec/KB * KB + 1 sec
    If we assume a transaction is 500 bytes or 1/2 KB, we get the function

    Network latency (sec) = 19/600 sec/tx * tx + 1 sec

We use this as a parameter into our exponential delay
'''
SEC_PER_TRANSACTION = 16.0/600