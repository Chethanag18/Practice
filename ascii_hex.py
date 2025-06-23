def string(s):
    result = ""
    for i in s:
        h = format(ord(i) , "x")
        result += h + " "
    return result.strip()
print(string("hello"))