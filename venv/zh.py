import math as m
def tra(func,a,b,nseg):
    dx=1.0*(b-a)/nseg
    sum=0.5*(func(a)+func(b))
    for i in range(1,nseg):
        sum+=func(a+i*dx)
    return sum*dx
f= lambda x: 2*x + 1  /(m.sqrt(x+3))

a=tra(f, 0,1, 100)
print(a)
