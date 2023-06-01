# Python code
# To print even length words in string

#input string
n="its my first program in python"
#splitting the words in a given string
s=n.split(" ")
for i in s:
  #checking the length of words
  if len(i)%2==0:
    print(i)
