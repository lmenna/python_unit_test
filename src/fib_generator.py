# fib_generator.py
#
# Shows how to generate the Fibonacci secquence using a Python generator
#
# The definition of the sequence is,
#
# Here is the sequence: 0,1,1,2,3,5,8,13,21,...
#
# x0 = 0
# x1 = 1
# x2 = 1
# :    :
# x(n) = x(n-1) + x(n-2)
#

def gen_fib():
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b




