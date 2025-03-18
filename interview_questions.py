#Function that reverses a string
def reverse_string(word):
    return ''.join(reversed(word))
#Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "Hello"
    #Perform the reverse operation
    reversed_str = reverse_string(input_str)
    #Check if the reverse string matches expected output
    assert reversed_str == "olleH"
    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)

#Function to check for palindrome
def is_palindrome(word):
    #Reverse the string using reversed() and join()
    reversed_str = ''.join(reversed(word))
    return word == reversed_str
#Test. Verification of is_palindrome function
def test_is_palindrome():
    #Define the input string
    input_str = "racecar"
    #Perform the palindrome check
    result = is_palindrome(input_str)
    #Check if the result is True for a palindrome
    assert result == True
    print("Test Passed!" + input_str + " is a palindrome.")

#Import math module to access functions
import math
def compute_factorial(number):
    #Compute the factorial of "number" using built-in factorial function from math module
    return math.factorial(number)
#Test. Verification of compute_factorial function
def test_compute_factorial():
    #Define input number
    input_number = 5
    #Perform factorial computation
    result = compute_factorial(input_number)
    #Check if the result is equal to expected factorial value
    assert result == 120
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))