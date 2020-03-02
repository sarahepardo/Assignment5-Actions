import unittest
import task
import math
from datetime import date



class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

class TestCaseA(unittest.TestCaseA):

    def test_getarea(self,radius):
        self.assertEqual(radius=13, area=530, expected="true")

class TestCaseB(unittest.TestCaseB):

    def test_firstlastlist(self,List):
        apple=[4, 2, 9, 1]
        self.assertTrue(apple,first=4)
        self.assertTrue(apple,last=1)

class TestCaseC(unittest.TestCaseC):

    def test_differencedays(self,fyr,fmon,fday,lyr,lmon,lday):
        fyr=2020
        fmon=1
        fday=14
        lyr=2020
        lmon=2
        lday=17
        first=date(fyr,fmon,fday)
        last=date(lyr,lmon,lday)
        self.assertTrue(last-first == 35,"true")


if __name__ == '__main__' :
    unittest.main()
