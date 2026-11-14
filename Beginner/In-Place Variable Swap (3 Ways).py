# In-Place Variable Swap (3 Ways)
# Given two variables a = 42 and b = 99, 
# swap their values without using a third temporary variable in three separate ways: 
# using Python's tuple unpacking, 
# using addition/subtraction, 
# and using the bitwise XOR (^) operator.

a = 42
b = 99

def first_method(a,b):
    a,b = b,a
    return a,b

def second_method(a,b):
    a = a + b
    b = a - b 
    a = a - b
    return a,b

def third_method(a,b):
    # 42 = 00101010 | 101010
    # 99 = 01100011 | 1100011
    a = a ^ b
    b = a ^ b 
    a = a ^ b
    return a,b


"""
converting bit to integer in python is 
int('Binary bits not starting with zero',2 <- this indegates that it is a binary number)

"""
print(f'Original value of a = {a} and b = {b}')
print(first_method(a,b))
print(second_method(a,b))
print(third_method(a,b))