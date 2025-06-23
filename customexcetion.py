class TooSmallValue(Exception):
    pass
value = int(input())
try:
    if value < 10:
        raise TooSmallValue("Number is smaller than 10")
    else:
        print(value)
except TooSmallValue as e:
    print(e)
    