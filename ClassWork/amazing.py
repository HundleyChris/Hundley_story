"""
This program demonstrates IMPORT statments and LOOPS
"""
#import statments go first
import time

#for variableName in range(start, stop, step):
#OR
# for variableName in range(stop): *this will start at 0 and step by 1
for i in range (1, 11):
    print("Thanos Car" + str(i))
    
#Count to 100 by 5's

for i in range(1, 21):
    print(int(str(i)) * 5)
#OR
for i in range(5,101,5):
    print(str(i))
#count down from (start at 20) by 2's and stop at -4
for i in range(20, -6 , -2):
    print(str(i))