a = []
size = int(input("Enter the size of an array"))
print("Enter the values of array")
for i in range(0, size):
    values = int(input())
    a.append(values)

for i in range(0, size):
    for j in range(0, size):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)

