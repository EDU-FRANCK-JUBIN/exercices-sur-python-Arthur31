pi = 3.14159

myPi = 1.

for i in range(1, 1000000000):    
    myPi *= (4*i**2)/((4*i**2)-1.)
    # P = P * t
myPi *= 2

print(myPi)