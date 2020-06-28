# Start Program
"""
Program: test_dict_membership.py
Author: Paul Thairu
Last date modified: 06/23/2020

"""
import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass

    # assertion for an item in the set (expect True)
    def test_in_in_set_true(self):
        new_set = {4, 5, 6}
        element = 6
        self.assertTrue(dict_membership.in_dict(new_set, element))

    # assertion for an item in the set (expect False)
    def test_in_self_false(self):
        new_set = {2, 3, 4}
        element = 5
        self.assertTrue(not dict_membership.in_dict(new_set, element))


if __name__ == '__main__':
    unittest.main()

# End program
