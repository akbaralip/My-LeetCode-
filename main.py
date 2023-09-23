a = []
size = int(input("Enter Array Size"))
print("Enter Values")
for i in range(0, size):
    values = int(input())
    a.append(values)
print(a)
array2 = a.copy()

print(array2)

Size = int(input("Enter a Size"))
print("Enter Values")
for j in range(0, Size):
    Values_2 = int(input())
    array2.append(Values_2)
    array2.sort()
print(array2)