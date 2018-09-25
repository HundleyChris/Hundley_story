import time

x = int(input("Enter a number to count downfrom. "))
for i in range(x,0,-1):
    print(i)
    time.sleep(1)