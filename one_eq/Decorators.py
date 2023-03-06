def square(f):
    def inner():
        x = f(y)
        return x**2
    return inner

@square
def f(x):
    return x+1

a = f()
print(a(2))



