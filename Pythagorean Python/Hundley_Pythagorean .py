"""
Write a program that will ask the user to
enter their name and respond with a greeting using this name.
"""
name = input("Hello Mr/Ms what is your name.")
print("Hello " + name + " nice to meet you.")

a = int(input("Give me the A for the pythagorean thearm."))
b = int(input("Give me the B for the pythagorean thearm."))
A = int(a**2)
B = int(b**2)
C = int(A+B)
answer = float(C**(1/2))
print("The C of the equation will be " + str(answer) + ".")