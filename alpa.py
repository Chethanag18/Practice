"""Please write a program which accepts a string from console and print the characters that have even indexes.
Example: If the following string is given as input to the program:"""
a = "H1e2l3l4o5w6o7r8l9d10"
store = ""
for i in a:
    if i.isalpha():
        store += i
print("".join(store))
