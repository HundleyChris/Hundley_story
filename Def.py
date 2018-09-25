import random 
def David():
    even = 0
    for i in range (0,10):    
        x = random.randint(1,100)
        if (x%2 == 0):
            print("The number " + str(x) + " is even.")
            even += 1
        else:
            print("The number " + str(x) + " is odd.")
    print("The even added equals " + (str(even)) + ".")

def greeting():
    x = input("Hello what is your fortnite username?")
    print("Hello " + str(x) + ".")
David()

def age():
    age = int(input("What is your age so we can determine if you can vote."))
    return age
    