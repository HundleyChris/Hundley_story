def greeting():
    print("Hello world")
    
    
greeting()

def ASKname():
    name = input("What is you name? ")
    print("Hello " + name + " how are you?")
    
    
    
    
ASKname()


def ASKname2():
    name2 = input("What is you name? ")
    return name2
    
    
    
    
x = ASKname2()
print("Hello " + x)

        
        
        
def agedef():
    age = int(input("What is your age? "))
    return age
def canVote(age):
    if(age>= 18):
        print("You can vote!")
        canVote = True
    else:
        print("Sorry you cant vote.")
        canVote = True
    
    
    
y = agedef()
canVote(y)
print(y)