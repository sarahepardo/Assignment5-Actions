import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

class TestCaseA(unittest.TestCase):

    def test_getarea(self,radius):
        self.assertEqual(radius=13, 530, "true")

class TestCaseB(unittest.TestCase):

    def test_firstlastlist(self,List):
        apple=[4, 2, 9, 1]
        self.assertTrue(apple,first=4)
        self.assertTrue(apple,last=1)



if __name__ == '__main__' :
    unittest.main()
    test_getarea()