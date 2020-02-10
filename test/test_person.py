# test_application_code.py
#
# Example of unit testing using the built in Python unittest.
#
# To run the unit test use the command,
#
# > python -m unittest test_person
#

import unittest

from src.person import Person

class Testing(unittest.TestCase):

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_person(self):
        p = Person()
        the_name = "Luigi"
        p.set_name(the_name)
        self.assertEqual(p.get_name(0), the_name)

if __name__ == '__main__':
    unittest.main()

