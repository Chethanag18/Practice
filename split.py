def text(string, width):
    for i in range(0, len(string), width):
        print(string[i:i+width])

S = input()
W = int(input())
text(S, W)
