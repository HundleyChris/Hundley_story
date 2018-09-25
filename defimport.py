import Def

Def.David()
Def.greeting()
x = Def.age()

if (x >=18):
    print("you can vote.")
else:
    print("You can not vote.")
    print("In " +str(18 - x) + " years, you will ba able to vote.")