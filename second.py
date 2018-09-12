"""
Triple quotes will allow me to comment out multiple line.

Write a progam that will ask the user what their age is and then 
determine if they are old enought to vote or not and respond appropriately
"""
print("what is your age  so we can determine if you could vote?")
Age = input()
if Age < 18 :
    print("Well then you can vote.")
if Age > 18 :
    print("Well then go back to your mommy.")
    