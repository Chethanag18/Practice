"""def find_extra_char(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    for c1, c2 in zip(s1_sorted, s2_sorted):
        if c1 != c2:
            return c2
    return s2_sorted[-1]  
print(find_extra_char("eueiieo", "iieoedue")

def is_shadow_sentence(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    if len(words1) != len(words2):
        return False
    for w1, w2 in zip(words1, words2):
        if len(w1) != len(w2) or set(w1) & set(w2):
            return False
    return True
is_shadow_sentence("they are round", "fold two times")

def dupl_letters(sentence):
    for word in sentence.split():
        if len(set(word)) != len(word):
            return True
    return False
dupl_letters("this is cool")  
dupl_letters("no duplicates")

def ascii_to_hex(s):
    return ' '.join(format(ord(c), '02x') for c in s)
    
def blocking_spot(a, b):
    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in winning_lines:
        if a in line and b in line:
            for pos in line:
                if pos != a and pos != b:
                    return pos

def has_friday_13(month, year):
    import datetime
    return datetime.date(year, month, 13).weekday() == 4
    
    

def outer_function():
    x = 10
 
    def inner_function():
        nonlocal x  
        x = 20     
        print("Inner:", x)
 
    inner_function()
    print("Outer:", x)

def ascii_to_hex(s):
    return ' '.join(map(lambda c: format(ord(c), '02x'), s))"""
