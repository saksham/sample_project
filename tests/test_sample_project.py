#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sample_project
----------------------------------

Tests for `sample_project` module.
"""

import unittest

from sample_project import sample_project


class TestSample_project(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert 2 == 3

    def test_something_else(self):
        print "I am running something else"
        assert 3 == 4

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()