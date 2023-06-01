# Python program to check
# if a string is palindrome
# or not

a = "india"

k = ""
for i in a:
    k = i + k

if (a == k):
    print("Yes")
else:
    print("No")
