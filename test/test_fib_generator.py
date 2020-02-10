# test_fib_generator.py
#
# Example of unit testing using the built in Python unittest.
#
# To run the unit test use the command,
#
# > python -m test_fib_generator
#
import unittest

from src.fib_generator import gen_fib

class Testing(unittest.TestCase):

  def test_fib(self):
    f_gen = gen_fib()
    # Generate the first 20 Fibonacci numbers
    fibs = [next(f_gen) for _ in range(20)] 
    self.assertEqual(fibs[19], 6765)

if __name__ == '__main__':
  unittest.main()
