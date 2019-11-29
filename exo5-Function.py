def max (a, b):
    if a>b:
        return a
    else:
        return b


print(max(10, 5))
print(max(5, 10))



def max2 (a, b, c):
    maxAB = max(a, b)
    maxBC = max(b, c)
    return max(maxAB, maxBC)

print(max2(10, 5, 2))
print(max2(5, 10, 2))
print(max2(2, 5, 10))
print(max2(5, 3, 10))




def closure(num):
    return num*2-1


print(closure(5))
print(closure(6))
print(closure(7))