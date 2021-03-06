#!/usr/bin/python
# -*- coding: utf-8 -*-
import minitest
import sys


class TestDemo(minitest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print ("this setupclass() method only called once.\n")

    # @classmethod
    # def tearDownClass(cls):
    #     print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.")

    def tearDown(self):
        print ("do something after test : clean up.")

    def test_add(self):
        """Test method add(a, b)"""
        assert 1+2 == 3

    def test_minus(self):
        """Test method minus(a, b)"""
        assert 5-3 != 2

    def test_three(self):
        """Test exception"""
        raise Exception("test exception")


if __name__ == '__main__':
    # loader = minitest.TestLoader()
    testsuite = minitest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    runner = minitest.TestRunner()
    result = runner.run(testsuite)