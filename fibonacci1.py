a = 0
b = 1
n = int(input("Enter the number of elements in the series: "))

for i in range(n):
    print(a, end = " ")
    a, b = b, a + b
    6