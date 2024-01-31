import numpy as np

def testExample1():
    x = np.arange(10).reshape(2,-1)
    result = np.logical_and(x>3, x<7).sum(0)
    print(result)

if __name__ == '__main__':
    testExample1()



