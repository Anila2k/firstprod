#a = [23, 344, 243, 2, 442442, 42, 4, 8667]
'''
for i in range(len(a)):
    print("текущий индекс", i)
    print("текущий элемент", a[i])

b = 0
c = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        b += 1
    else:
        c += 1
print(b, c)
'''
a = [5, 3, 4, 2, 3, 4, 5, 2, 5,]
c = 0
b = 0
for i in range(len(a)):
    if a[i] >= 1 and a[i] <= 5:
        c += a[i]
        b += 1
print(c / b)
