l = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    l.append(int(input("Enter the element: ")))

s = int(input("Enter the element to search: "))

for i in range(n):
    if l[i] == s:
        print(s, "found at position", i + 1)
        break