def string(s):
    parts = s.split('0')
    cleaned_parts = []
    for p in parts:
        if p != '':
            cleaned_parts.append(p)
    parts = cleaned_parts
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
print(string("Chethana0000Gadigesh00000456"))