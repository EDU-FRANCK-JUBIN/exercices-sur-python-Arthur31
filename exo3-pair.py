tt= [32, 5,8,3,75,2,15]

pair = []
impair = []

for num in tt:
    if num % 2:
        impair.append(num)
    else:
        pair.append(num)


print("Pair : ", end=' ')
print(pair)
print("Impair : ", end=' ')
print(impair)