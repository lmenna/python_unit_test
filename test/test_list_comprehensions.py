# test_list_comprehensions.py
#
# Example of unit testing using the built in Python unittest.
#
# To run the unit test use the command,
#
# > python -m test.test_list_comprehensions
#
# Run that from the unit_testing directory

import unittest

from src.list_comprehensions import create_cubes_comprehension
from src.list_comprehensions import create_cubes_loop
from src.list_comprehensions import create_odd_cubes

class Testing(unittest.TestCase):

  def test_list_comprehensions(self):
    num_cubes = 5
    cubes_loop = create_cubes_loop(num_cubes)
    cubes_comprehension = create_cubes_comprehension(num_cubes)
    for i in range(num_cubes):
      self.assertEqual(cubes_loop[i], cubes_comprehension[i])

  def test_odd_cubes(self):
    max_num = 20
    odd_cubes = create_odd_cubes(max_num)
    self.assertEqual(odd_cubes[2], 5**3)
    self.assertEqual(len(odd_cubes), 10)
    
if __name__ == '__main__':
  unittest.main()

