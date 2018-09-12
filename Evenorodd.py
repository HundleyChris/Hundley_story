"""
Write a program that will take a number (Integers only) and 
return a statement that will let the user know if it si even or odd
"""
number = int(input("Tell me a number and i will determine if it is even or odd."))
if (number % 2 == 0):
    print("That is even.")
if (number % 2 == 1):
    print("That is odd.")