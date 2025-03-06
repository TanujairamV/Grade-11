str = 'lol'
p = ''
for i in range(len(str)-1, -1, -1):
    p += str[i]
if str == p:
    print(str,"is Palindrome")