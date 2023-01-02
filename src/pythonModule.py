import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci().title)

from pkg.fibonacci import Fibonacci as fb

Fibonacci.fib(1000)

print("ex3 : ", Fibonacci.fib2(1600))
print("ex3 : ", Fibonacci().title)

import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

from pkg.calculations import div as d

print("ex5 : ", int(d(100, 10)))

import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))