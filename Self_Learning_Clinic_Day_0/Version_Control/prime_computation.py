'''
 A PRIME NUMBER IS A WHOLE NUMBER GREATER THAN 1 WHOSE ONLY
 TWO WHOLE-NUMBER FACTORS ARE 1 AND ITSELF

 EXAMPLES: 2,3,5,7,11,13,17,19,23
'''
from test_file import PrimeNumberTest
import unittest

def prime_computation(self, value):
    #if value keyed in is greater than 1
    if value > 1:
        for i in range(2, value):
            if (value%i == 0):
                print("Invalid Prime Number")
                break
            else:
                print("Valid Prime Number")

    #else the value is less than 1
    else:
        print("Invalid Prime Number")

if __name__ == 'main':
    number = int(input("Enter a number to see if it is a prime number"))

    #Computation Results
    prime_computation(number)
    #Echo Unit Testing Results
    unittest.main()

