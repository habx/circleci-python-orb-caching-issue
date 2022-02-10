#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main file test"""


import unittest


class MainTest(unittest.TestCase):
    """main test"""

    def test_hello(self):
        """test hello"""

        self.assertEqual("Hello, world!", "Hello, world!")


if __name__ == '__main__':
    unittest.main()
