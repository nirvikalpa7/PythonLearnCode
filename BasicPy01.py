"""Multy lines
comment,
This is an
example, true, true, true"""

# This program says hello and asks for my name
print('Hello, world!')
print('What is your name?')  # ask for their name

myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age

myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Example of dynamic data types
string = """
Example of text multyline
12345
777
999999
"""
print(string)

string = 12345
print(string)

string = ["list", "1111", "2222", "list"]
print(string)

string = {10: "dict1", 33: "foo", 77: "bar"}
print(string)
