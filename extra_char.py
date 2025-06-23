def extra_char(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):  
        if s1[i] != s2[i]:
            return s2[i]
    return s2[-1]  
print(extra_char("abc","abc"))