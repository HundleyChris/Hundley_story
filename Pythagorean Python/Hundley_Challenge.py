print("Give me the three legs of a triangle, going in order A,B,C.")
print("I will determine if it is not triangle, right triangle, obtuse triangle, and acute triangle.")
a = int(input())
b = int(input())
c = int(input())
Asquare = int(a**2)
Bsquare = int(b**2)
Csquare = int(c**2)
AB = int(Asquare + Bsquare)
if(Csquare > Asquare + Bsquare):
    print("The triangle is Obtuse.")
if(Csquare < Asquare + Bsquare):
    print("The triangle is Acute.")
if(Csquare == Asquare + Bsquare):
    print("The triangle is right trinagle.")    
else:
    print("This is not a triangle.")