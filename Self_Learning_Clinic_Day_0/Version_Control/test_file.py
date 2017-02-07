
import unittest
from prime_computation import prime_computation

class PrimeNumberTest(unittest.TestCase):

    #1. Ensure correct computation is done: U0BeTfXW5JWI8dvpDA5q1LUMgAk1
    def testSuccess(self):
        answer = prime_computation(2)
        self.assertEqual(answer, True, outputMsg="Valid Prime Number")

    #2. Instance of failure in computation
    def testFailure(self):
        answer = prime_computation(1)
        self.assertEqual(answer, False, outputMsg="Invalid Prime Number")

    #3. Ensure correct type is supplied
    def testValidArguments(self):
        answer = prime_computation("onetwo")
        self.assertEqual(answer, False, outputMsg="Invalid Argument Provided")

    #4.Ensure value is greater than 1
    def testForOne(self):
        answer = prime_computation(-1)
        self.assertEqual(answer, False, outputMsg="Invalid Prime Number")

    #5.Ensure that zero is not provided
    def testForNumberZero(self):
        answer = prime_computation(0)
        self.assertEqual(answer, False, outputMsg="Invalid Prime Number")

    #6. Can Work with Large Numbers
    def testForLargeNumbers(self):
        answer = prime_computation(79)
        self.assertEqual(answer, True, outputMsg="Valid Prime Number")

    #7. Test Invalid Large Number
    def testInvalidLargeNumber(self):
        answer = prime_computation(72)
        self.assertEqual(answer, False, outputMsg="Invalid Prime Number")

    #8. Test is items were returned
    def testReturnValue(self):
        answer = prime_computation(" ")
        self.assertEqual(answer, False, outputMsg="Invalid Prime Number")
