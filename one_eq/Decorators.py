import numpy as np 

def square(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)**2
    return inner

@square
def func(x):
    return np.sin(x)

if __name__ == "__main__":
    print(func(np.pi/4))




