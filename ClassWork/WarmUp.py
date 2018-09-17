"""
Write a program that will ask the user for a number(integers only)
and return a statemnt that the number is EVEN of ODD.
"""
number = input("Give me a number. I will determine if it is even or odd.")
if(number%2 == 0):
    print("That number " + str(number) + " is even.")
if(number%2 == 1):
    print("That number " + str(number) + " is odd.")
#OR you can use and else statement